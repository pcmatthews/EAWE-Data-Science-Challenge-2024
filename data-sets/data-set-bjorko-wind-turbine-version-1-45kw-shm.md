# Data set "Björkö Wind Turbine Version 1 (45kW) SHM"

## The data set

The Chalmers wind turbine has variable speed operation with a direct driven generator and a frequency converter, it also has a digital control system developed by Chalmers. The wind turbine has a rated power of 45 kW and rated speed of 75 rpm. The wooden tower is 30 m high, the blades of carbon fibres are 7.5 m long, and the turbine diameter is 15.9 m. The individually blade pitch system is electrical. The turbine is situated on the island Björkö at Skarviksvägen, 20 km west of Göteborg city. The coordinates are: 57.71818820625921, 11.683382148764485.

69 SCADA and structural vibration and loads Channels timeseries (sampled at 20 and 100 Hz) such as nacelle accelerations, tower and blades bending moments are included.

Structured metadata about wind turbine characteristics, SCADA, vibration and loads channels are included as JSON files and CSV.

This particular dataset consisting of high frequency sampled data, is intended for condition and structural health analysis.

**The data covers:**

* the measurements sampled at 100 Hz correspond to the period from 05 July 2022 to 9 June 2023
* the measurements sampled at 20 Hz correspond to the period from 05 July 2022 to 2 August 2023

**This repository includes:**

**Time-series data in csv format:**

* B1\_CL4\_20.csv (this is the data sampled at 20 Hz)
* B1\_CL4\_100.csv (this is the data sampled at 100 Hz)

**Metadata:**

* Bjorko\_Sensors\_Specs\_Metadata.csv (Sensors signals specification in csv format)
* Bjorko\_modes\_mapping.csv (numerical integer value representing the wind turbine controller system mode in csv format)
* Bjorko\_modes\_mapping.json (numerical integer value representing the wind turbine controller system mode in csv JSON format)
* Bjorko\_digital\_io\_states\_mappings.csv (Description of digital input and output states in the wind turbine controller system in csv format)

**Media:**

* Chalmers-Wind turbine.pdf (description of the wind turbine including pictures)
* Chalmers wind turbine description 220121-short.pdf (description of the wind turbine including pictures)

**Semantic artifacts:**

* N/A

**Other:**

* N/A

## Data access

The data can be accessed on Zenodo [HERE](https://zenodo.org/record/8230330).

## Further information

More information about the wind turbine can be found [here](https://eawe.eu/site/assets/files/downloads/committees/twtc/TWTC-chalmers-twt-facilities.pdf).
