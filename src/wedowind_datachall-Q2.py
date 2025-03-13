# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 10:47:04 2025

wedowind_datachall.py

WeDoWind 2024-25 data challenge: Sub Chall 2 (speed-torque) a very basic attempt

https://github.com/WeDoWind/EAWE-Data-Science-Challenge-2024/blob/main/challenge-description.md

Note: use data between 22-23 Sept 2022
This maps onto indices 

Submissions details:
    PARTICIPANT_ID = 8 (Github: pcmatthews)
    

Created on Thu Feb 27 11:53:02 2025

@author: Peter Matthews (p.c.matthews@durham.ac.uk)
"""

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

# load the data (will it fit?)

data = pd.read_csv("B1_CL4_20.csv", nrows=1600000) # limit to ca just after 23 Sept 2022, that's all that's needed for Ch 2
#data = pd.read_csv("B1_CL4_20.csv", nrows=100) # limit to small debeug 
#data = pd.read_csv("B1_CL4_20.csv") # EVERYTHING!


# time index
d1904 = dt.datetime(1904,1,1,0,0) # midnight 1 Jan 1904 (start of time), use timedelta(seconds=t) to get date
DateTime = data.Time.apply(lambda t: (dt.timedelta(seconds=t) + d1904))

data.insert(0,'DateTime', DateTime)


# add some additional calculated values (these are not used for Challenge 2)

data['mechpwr'] = data.TurbSpeed2 * data.RST2 # mechanical power
data['epwr'] = data.DCC * data.DCV # electrical power

data['WSma'] = np.convolve(data.WS30, np.ones(600*20)/(600*20), mode='same') # WS moving average, 10 mins


# Filter down to test range 22-23 Sept 2022

d_bot = data.DateTime > dt.datetime(2022,9,22,0,0)
d_up = data.DateTime < dt.datetime(2022,9,23,23,59)
d_range = d_up & d_bot

data_range = data[d_range]

# plot

data_range.plot(x='TurbSpeed2', y='RST2', kind='scatter', title='Sub Challenge 2 date range')
plt.show()

# filter out on torque (below -1000, above +7000)

d_bot = data.RST2 > - 1000
d_up = data.RST2 < 7000
d_filter = d_bot & d_up

data_filter = data_range[d_filter]

# and plot
data_filter.plot(x='TurbSpeed2', y='RST2', kind='scatter', title='Sub Challenge 2 date range, torque filter')
plt.show()

# Now train initial mapping from Turbine Speed to Torque
# Train non-parametric regression

from sklearn.neighbors import KNeighborsRegressor

# Extract RPM and torque
x = np.array(data_filter.TurbSpeed2).reshape(-1,1) # needs to be an array of arrays
y = np.array(data_filter.RST2) # target

# set up model

model = KNeighborsRegressor(n_neighbors=10, weights='uniform') # params guessed
model.fit(x,y)

x_range = np.linspace(0, 80, 100).reshape(-1,1)
y_est = model.predict(x_range)

# plot
plt.figure()
data_filter.plot(x='TurbSpeed2', y='RST2', kind='scatter', title='Regression full (interim)')
plt.plot(x_range, y_est, c='r')

plt.show()

# Next filter to remove points 'far' away from regression, and then retrain

t_est = model.predict(x)
t_res = y-t_est # compute residue
data_filter['t_residue'] = t_res

d_filt2 = np.abs(data_filter.t_residue) < 500 # guess that 500 is enough

data_filter2 = data_filter[d_filt2]

#retrain, replot
x = np.array(data_filter2.TurbSpeed2).reshape(-1,1) # needs to be an array of arrays
y = np.array(data_filter2.RST2) # target

model2 = KNeighborsRegressor(n_neighbors=10, weights='uniform') # params guessed
model2.fit(x,y)

x_range = np.linspace(0, 80, 100).reshape(-1,1)
y_est = model2.predict(x_range)

# plot
plt.figure()
data_filter2.plot(x='TurbSpeed2', y='RST2', kind='scatter', title='Regression filter final')
plt.plot(x_range, y_est, c='r')

plt.show()


# create CSV file with lookup TurbSpeed2 -> RST2

fname = "Sub-challenge-2_8_1.csv" # last digit is the submission number

# create dataframe with lookup
x_range = np.linspace(0,data_filter2.TurbSpeed2.max(), 100).reshape(-1,1)
y_est = model2.predict(x_range)

submit = pd.DataFrame({'TurbSpeed2':x_range.ravel(), 'RTS2':y_est})


submit.to_csv(fname,index=False)

