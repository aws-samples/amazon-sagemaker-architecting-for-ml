# NLP: Text Classification

## Business Problem
Building and producing products that are actually adopted by customers and solve real problems for them is a historically challenging task. Today, imagine that you have joined the machine learning team on the Amazon e-commerce site! Your webpage is full of reviews from customers for each of your products. Your product owners want to know about a negative review *immediately*. Ideally, they'd like to know why the review was negative. 

## Topic Modeling
Your research team just finished labeling a set of data for positive and negative reviews. Go ahead, you can put it into a model right away. It should work straight out of the box!

Your task is to identify topics, especially the negative ones. Download the data set as listed below, and extract the negative rewivews.

Next, load them into Amazon Comprehend. Spend some time reading about Comprehend here:
- https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html 

You can either do this through the console, or programatically from your notebook. If you're doing this from your notebook, just make sure you attach the Comprehend role directly to your SageMaker execution role. 

After you've extracted the topics, spend some time reading through them. Do they seem logical? Can you describe them in English, give it a try, it's pretty tough!

## Second Phase of Topic Modeling
After using Comprehend, you can go one of two routes. In advanced cases, you can do both!

(1) Build your own topic modeler. SageMaker has two built-in topic modeling algorithms: Latent Dirichlet Allocation and Neural Topic Modeling. Pick one or both of them, and train your data in them. What do the resulting topics look like, are they better or worse than the ones you found in Comprehend? 

(2) Re-label your data. With sub-categories identified, or with a smaller subset of the most relevant ones, can you add additional labels to your data? Extra points for using SageMaker Ground Truth for this. Can you build accurate models that can identify the sub-categories?


## Data Sets 
The dataset you'll be working with comes directly from the Amazon review site. This is hosted on AWS through coursework via fast.ai https://course.fast.ai/datasets. Navigate to this page and click download for **Amazon Reviews: Polarity**. The Amazon reviews polarity dataset is constructed by taking review score 1 and 2 as negative, and 4 and 5 as positive. Samples of score 3 is ignored. In the dataset, class 1 is the negative and class 2 is the positive. Each class has 1,800,000 training samples and 200,000 testing samples. 

# Existing Research 
Your research team just developed an innovative model that uses convolution to classify text. See this page for further details. http://xzh.me/docs/charconvnet.pdf 

# Sample Code 
Code from your researchers is available here. https://github.com/zhangxiangxiao/Crepe 
Download your data from the site, upload it to an s3 bucket via the AWS console, and then run this block of code on your SageMaker notebook instance to read the data into a pandas data frame. 

```python
import pandas as pd

!mkdir /Data
!aws s3 cp s3://nlp-workshop-reviews/amazon_review_polarity_csv.tgz /Data
!tar -xvzf Data/amazon_review_polarity_csv.tgz
df = pd.read_csv("amazon_review_polarity_csv/train.csv", names=["Label", "Title", "Review"])
```
