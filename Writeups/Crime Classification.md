# Deep Learning Crime Classification
Welcome to the CPD! You've just joined the Chicago Police Department, and their first task for you is non-trivial. They want you to build a deep learning model to predict crime in the city.

## Datasets
You'll leverage data that exists on the Chicago Data Portal. Join this with weather data from NOAA, make sure you keep track of temperature and precipitation. 
- https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2  
 - https://www.ncdc.noaa.gov/cdo-web/ 

## Deep Learning
In this case, we want you to build a deep learning model. If you're unfamiliar, learn about sequential models that are built into Keras from this link:

    - https://keras.io/getting-started/sequential-model-guide/ 

## Analysis
1. First, analyze the data by finding trends. Are there periods where crimes repeat themselves on blocks? Which blocks see the most types of crime? What is the cycle period where crimes return on each block? Seven days, one month, one year?
2. Identify key crimes that you want to predict, selecting between 3 and 10. 
3. Clean your data, scale it to have similar max/mins. 

## Modeling
Build a number of deep learning models, using Keras. Focus on LSTM's. Does the sequential element help us see which crime is most likely to occur more precisely?

## Existing Work
- https://arxiv.org/pdf/1806.01486.pdf  
