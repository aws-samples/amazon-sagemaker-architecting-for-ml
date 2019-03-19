# Product Recommendation Engines

*Business Case*
Financial firms offer a wide array of products: checking accounts and retirement plans are just the beginning. Today, you have joined the ranks of the data scientists at Santander.  Your current website provides a large number of recommendations to a small number of customers, which means that your company is not taking full advantage of the data sets your currently own and maintain. If you could recommend the right product to the right customer, you could accelerate your growth and meet the real demands of your consumer base.

*Machine Learning Method*
In this project, you will learn about Factorization Machines. This is a highly scalable algorithm that was developed by Steffen Rendel in 2010. It has the capacity to leverage extremely large datasets at the Terabyte scale, while still training in linear time. 

![alt text](Images/recommender_1.png ) 

In essence, the factorization machines model is calculating the dot product between the user information and the item information, then computing the difference between those to update the model.

![alt text](Images/recommender_2.png ) 


In order to accomplish this, you'll need to *format your data as events*. Each row in your final data set will need to be a single point in time when a customer interacts with a product account. Each column will be either a binary indicator for the product/user, or another feature.

*Data set description*
We highly suggest using the Movie Lens dataset. This is well suited to recommendation problems and should be available from public sources.

*A follow up note on method*

* The built-in algorithm you are working with is designed to only handle either binary classification or regression. It can be extended to provide multi-class classification with KNN. First start with the recommender, and if your are up to the task, consider extracting the matrix and using it to build KNN clusters.

*References*

* In Python: https://www.datacamp.com/community/tutorials/recommender-systems-python
* Intuitively: https://www.analyticsvidhya.com/blog/2018/01/factorization-machines/ 
* Formally: https://www.csie.ntu.edu.tw/~b97053/paper/Rendle2010FM.pdf 

