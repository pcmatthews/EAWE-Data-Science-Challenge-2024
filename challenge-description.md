---
description: Identifying controller settings from operational data
---

# Challenge description

## Background

In many practical situations of analysis of SCADA (and other operational data) supplied from commercial wind turbines, the lack of detailed knowledge of the turbine controller can pose a problem. This is especially the case when analysing data with high temporal resolution. To this end, this challenge addresses the need for methods for re-creating the turbine controller from SCADA data. For this, the Chalmers test turbine can be used as a test case, since the true controller setting and model is known. An additional usage can be to identify periods of changed operation in data where SCADA/operational data is incomplete (for example power curtailment, or turbine providing frequency control service).

## Goal

The goal of this challenge is to **develop new methods for identifying controller settings from operational data** based on 20 Hz data in the following aspects, which can be considered as sub-challenges:

* Sub-challenge 1: Identify controller parameters for a given architecture (e.g. finding the parameters of the NREL DISCON controller).
* Sub-challenge 2: Build a torque-rotor speed look-up table directly from the data.
* Sub-challenge 3: Identify instances when the controller goes to different modes of operation, for instance when running in frequency control service mode (i.e. when the parameters have been changed).
* Sub-challenge 4: Identify the pitch controller algorithm.

In the data set, one signal is the torque set-point (GenTorqSP). This signal is not to be used in the final solution, but can be used to evaluate solution methods.

## Available datasets

The challenge should be carried out based on the Chalmers 20 Hz data set found [here](https://relight.cloud/doc/data-set-bjorko-wind-turbine-version-1-45kw-shm-zfihk5/the%20eawe%20test%20turbine%20committee%20space). The SCADA data [here](https://relight.cloud/doc/data-set-chalmers-wrzncm/the%20eawe%20test%20turbine%20committee%20space) may be used for reference. Please use the following sub-sets of data for this challenge:

* For sub-challenge 1&2 and 4 use the data sets for Sept 22-23, 2022.
* For sub-challenge 3, the entire measurement period can be used.

## Submitting your results

The challenge starts on September 25th, 2024, and the submission deadline is **March 19th, 2025.** You can participate as follows:

1. **Register** yourself or your team as a participant [here](https://docs.google.com/spreadsheets/d/1xk85A-EoQaVacmndSnDZ1A7RE6NMClfhhk9To8Sm0q8/edit?usp=sharing). You will then have a PARTICIPANT\_ID. You only need to do this once.
2. Attend the _optional_ **monthly webinars** (every 4th Wednesday of the month at 15:00 CET) in order to ask questions, meet other participants and even form new teams.
3. Present your interim results at the _optional_ **interim webinar,** taking place on Jan. 22nd at 15:00 CET. To do so, you have to submit your interim results before then as explained in point 4.
4. **Submit your final results and present them at the final webinar on March 26th, 2025.** Do this by clicking on the “Reply” button at the top of this document. This will create a new document with a template and instructions, including how to upload the results files. You can save a draft at any time and work on the document again later. The submissions won't be assessed until after the submission deadline. This submission includes creating a Github branch for your code in our repository [here](https://github.com/WeDoWind/EAWE-Data-Science-Challenge-2024).
5. **Upload your results** [**here**](https://drive.switch.ch/index.php/s/thWhyljRVcvjXP5). Submit your results as a CSV file named "Sub-challenge-x\_PARTICIPANT\_ID\_N.csv" where N is your submission number (= 1 for your first submission) and x is the sub-challenge number. For example, if PARTICIPANT\_ID = 3, the first time you submit a result for sub-challenge 2, your file would be named "Sub-challenge-2\_3\_1.CSV".
6. **Fill out the participants' survey.** This will be made available later, and used to evaluate the WeDoWind project.

A failure to fulfill points 1, 4, 5 and 6 will result in immediate disqualification!

## Evaluation

The final report will be evaluated by our Evaluation Panel, consisting of:

* Sebastian Mulders, Delft University of Technology
* Ola Carlson, Chalmers University of Technology
* Håkan Johansson, Chalmers University of Technology
* Nikolay Dimitrov, DTU Wind

The following criteria will be considered:

* The reporting of the employed method and the novelty of the adopted approach.
* Sub-challenge 1: The error between the identified controller parameters and the actual controller parameters.
* Sub-challenge 2: The error between the submitted torque-rotor speed look-up table and the actual torque-rotor speed look-up table.
* Sub-challenge 3: The numbe rof correct instances when the controller goes to different modes of operation.
* Sub-challenge 4: The error between the submitted pitch controller algorithm and the actual pitch controller algorithm.

The submissions will be assigned overall scores and published as an anonymous ranking table on the Relight platform. First prize, second prize and third prize will be awarded, and each participant who submits a final report and fills out the participant survey will receive a participation certificate. The results will be published in a peer-reviewed journal.

## Participation guidelines

There is no restriction regarding what type of analysis methods or programming languages to use (C/C++, Matlab and Python are preferred). All code will fall under the LGPL V2 license. Further guidelines to make your code FAIR can be found in our GitHub repository [here](https://github.com/WeDoWind/EAWE-Data-Science-Challenge-2024).

## Disclaimer

The contestant takes the responsibility of obtaining any permission to use any algorithms/tools/data that are intellectual property of third party.
