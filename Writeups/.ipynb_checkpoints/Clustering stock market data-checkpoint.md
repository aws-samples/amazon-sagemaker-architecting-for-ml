# Clustering stock market data with ML Marketplace

Algorithmic trading - the devil is in the details. You've just joined the data science team for a new trading firm, All The Margins. Your firm has shown you their current portfolio, which they are quite pleased with. Your task is to find stocks that trade in a similar pattern to those in their existing portfolio. First, you will use the ML Marketplace to leverage a clustering solution. Next, you will enhance this by training your own model within SageMaker. 

**Goal**: Learn about approximate nearest neighbor identification in high-dimensional spaces via:

1. Clustering times series based on its shape using [K-Shape: Time Series Clustering](https://aws.amazon.com/marketplace/pp/Spotad-LTD-K-Shape-Time-Series-Clustering/prodview-bjbovimwn5ajs). 
2. Clustering high-dimensional data using Amazon SageMaker built-in [K-Means Algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/k-means.html)

#### Task 1 description:
In this task, you will learn how to perform clustering on time series data and identify stocks that are performing identical to each other over a given time-span. You will download the stock market data at runtime, normalize values for each stock, and then identify clusters of stocks with identical shape. You will then share findings about which stocks seem to have identical behaviors. You will also report which value for `k` returned you the minimum SSD (Sum of the squared distances between each data point and the cluster centroid). 

To help you ensure you have sufficient time for experimentation in Task 2, some [starter code](../Starter-Code/Apply clustering techniques (for workshop attendees).ipynb) for task 1 has been provided. 

#### *References:*

* https://aws.amazon.com/blogs/machine-learning/k-means-clustering-with-amazon-sagemaker/
* Accelerating ML projects with algorithms and models from AWS Marketplace (https://youtu.be/OrmHHVI1uPk?t=1682)
* [Interesting graphs] (https://github.com/awslabs/amazon-sagemaker-examples/blob/master/aws_marketplace/using_model_packages/financial_transaction_processing/Extracting_insights_from_your_credit_card_statement.ipynb)

#### Task 2 description:
In this task, you will learn how to identify approximate nearest neighbors in high-dimensional space by applying a clustering algorithm. As part of this task, you will first generate high-dimensional synthetic datasets containing trading portfolio tickers. You will then apply K-Means clustering algorithm and clusters traders that have identical portfolios. 

**Notes**:

* To make this a fun project, add tickers you have special interest in, to the list.
* Extra time left? 
    Explore other algorithms you can use to solve problems identified in Task 1 and 2 and compare the results using appropriate metrics.


#### *References:*

* https://aws.amazon.com/blogs/machine-learning/k-means-clustering-with-amazon-sagemaker/
* [How K-Means algorithm works](https://docs.aws.amazon.com/sagemaker/latest/dg/algo-kmeans-tech-notes.html)