# Predicting Airline Delays using SparkML & Sagemaker

## Introduction
The U.S. Department of Transportation's (DOT) Bureau of Transportation Statistics tracks the on-time performance of domestic flights operated by large air carriers. Using this data we would like to predict Flight delays

![flight delays](https://user-images.githubusercontent.com/1559391/56873334-3c3d4e00-69f7-11e9-8ed6-7f585bae5361.png)

## Project Goals
Your mission is two-fold. 
- Demonstrate how to use Spark for ETL and feature engineering on the input data. This will be the airline data and the *optional* Noaa data
- Leverage Sagemaker for model training and hosting

## Data sources
- On-time reporting data: You can download the zip by year/month
  - https://www.transtats.bts.gov/DL_SelectFields.asp?DB_Short_Name=On-Time&Table_ID=236


- Extra credit : Combine with weather data from NOAA to build a better model
  - https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/
  - https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/

## Machine Learning Method
There are multiple ways to approach this. 
- Classification to predict flight will be delayed or not
- Regression to provide a probability of a delay
- Ensemble learning using Random decision forests

## Presenting Results
Tenets
- Clearly defined Project Goal
- ETL strategy and why?
- Modeling strategy - describe the process of selecting the right model
- Path to production

Artifacts:
- PPT
- Code/Notebook walkthrough

Extra points
- Run a live demo with a custom UI 
- Using the NOAA weather

References:
- Spark Sagemaker examples - https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker-spark
- LinearLearner - https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html
- XGBoost - https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost.html
- Spark classification & Regression models - https://spark.apache.org/docs/2.2.0/ml-classification-regression.html
- Sagemaker Spark SDK - https://github.com/aws/sagemaker-spark
- Sagemaker Bring your own model -https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html
- Flight stats: https://www.flightstats.com/v2/global-cancellations-and-delays
- Pandas and Spark: https://koalas.readthedocs.io/en/latest/
- Spark & Sagemaker connection using SparkMagic : https://aws.amazon.com/blogs/machine-learning/build-amazon-sagemaker-notebooks-backed-by-spark-in-amazon-emr/
- If you need the access to data in s3, ask the instructors


