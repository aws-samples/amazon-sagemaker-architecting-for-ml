# Chicago-Crime
The Anti "Minority Report". To prevent criminal activity before it happens and save lives on both sides of the event. 

# Datasets
- Chicago Crime Data Sets: 
https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2
Includes:
    - Block
    - Location
    - Type of Crime
    - Description
    - Time 

- Weather in Chicago: NOAA will provide data from stations in Chicago on a daily basis for free.
https://www.ncdc.noaa.gov/cdo-web/. This includes primarily temperature maxs and mins. Most of the other fields are missing.

- Headlines? Social tension indicators?
- Gun availability indicators? 
- Gang rivalry indicators? 
- Housing price indicators; social status change data


# Modeling Strategy
- Break up events into types of crime. These are as follows. Each new day will be cross-referenced against a multi-class classification model that predicts each block for it's likelihood of having any of 7 types of criminal activity.
    - Kidnapping
    - Sexual assault 
    - Homocide
    - Motor vehicle theft 
    - Weapons violation
    - Battery
    - Theft
- Link with weather data
- Build a multi-class classifier to predict each type of crime
- Use sequential methods to model the add-on effect; because of what happened earlier in the year, this will happen. Most likely will need to model the sequence in a discrete window of time: One month? One quarter? One year? Will need to experiment here to find the right windo. 

Potentially use multi-class classification to rank blocks in the city based on their likelihood of having a type of crime in the coming day, given the weather forecast and all previously known criminal activity. 


Potentially use LSTM's to capture both the level of complexity and the sequential element. 

Open question: how do we standardize the sequence of both criminal events per block and weather events per block that lead up to the criminal event? Monthly? Yearly? For 2018 maybe just include the sequence of the last month. This means we need to chunk the data into month sequences that go into the LSTM's.

Is it actually better to think about this problem as forecasting? Where we're forecasting the level of crime? Unknown.

# End Goal
Heatmap that predicts crime multiple days in advance. Final system should be a website that queries the Chicago data portal and local weather sensors every day, retrains the model over night, and generates new predictions for the day's criminal activity.

Rather than getting side-tracked about the research goals, it might be more valuable to build the website first, and then load in new models over time as we ship them.
