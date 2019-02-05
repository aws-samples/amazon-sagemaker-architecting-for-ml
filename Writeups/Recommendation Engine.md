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
At your disposal, you have 1.5 years of consumer behavior. Your data begins in January 2015, and includes monthly records of customer activity. This includes credit card ownerships, savings account utilization etc. 

https://www.kaggle.com/c/santander-product-recommendation/data 

Your goal is to prediction additional products a customer will purchase in the final month, June 2016, given what they already have in the previous month. These products are the columns named: ind_(xyz)_ult1, which are the columns #25 - #48 in the training data. 

The test and train sets are split by time.

Column Name	Description
fecha_dato	The table is partitioned for this column
ncodpers	Customer code
ind_empleado	Employee index: A active, B ex employed, F filial, N not employee, P pasive
pais_residencia	Customer's Country residence
sexo	Customer's sex
age	Age
fecha_alta	The date in which the customer became as the first holder of a contract in the bank
ind_nuevo	New customer Index. 1 if the customer registered in the last 6 months.
antiguedad	Customer seniority (in months)
indrel	1 (First/Primary), 99 (Primary customer during the month but not at the end of the month)
ult_fec_cli_1t	Last date as primary customer (if he isn't at the end of the month)
indrel_1mes	Customer type at the beginning of the month ,1 (First/Primary customer), 2 (co-owner ),P (Potential),3 (former primary), 4(former co-owner)
tiprel_1mes	Customer relation type at the beginning of the month, A (active), I (inactive), P (former customer),R (Potential)
indresi	Residence index (S (Yes) or N (No) if the residence country is the same than the bank country)
indext	Foreigner index (S (Yes) or N (No) if the customer's birth country is different than the bank country)
conyuemp	Spouse index. 1 if the customer is spouse of an employee
canal_entrada	channel used by the customer to join
indfall	Deceased index. N/S
tipodom	Addres type. 1, primary address
cod_prov	Province code (customer's address)
nomprov	Province name
ind_actividad_cliente	Activity index (1, active customer; 0, inactive customer)
renta	Gross income of the household
segmento	segmentation: 01 - VIP, 02 - Individuals 03 - college graduated
ind_ahor_fin_ult1	Saving Account
ind_aval_fin_ult1	Guarantees
ind_cco_fin_ult1	Current Accounts
ind_cder_fin_ult1	Derivada Account
ind_cno_fin_ult1	Payroll Account
ind_ctju_fin_ult1	Junior Account
ind_ctma_fin_ult1	Más particular Account
ind_ctop_fin_ult1	particular Account
ind_ctpp_fin_ult1	particular Plus Account
ind_deco_fin_ult1	Short-term deposits
ind_deme_fin_ult1	Medium-term deposits
ind_dela_fin_ult1	Long-term deposits
ind_ecue_fin_ult1	e-account
ind_fond_fin_ult1	Funds
ind_hip_fin_ult1	Mortgage
ind_plan_fin_ult1	Pensions
ind_pres_fin_ult1	Loans
ind_reca_fin_ult1	Taxes
ind_tjcr_fin_ult1	Credit Card
ind_valo_fin_ult1	Securities
ind_viv_fin_ult1	Home Account
ind_nomina_ult1	Payroll
ind_nom_pens_ult1	Pensions
ind_recibo_ult1	Direct Debit

*Starter Notebook*

* Architecting-For-ML/StarterCode/Santander


*A follow up note on method*

* The built-in algorithm you are working with is designed to only handle either binary classification or regression. Consequentially, your first task will be to follow the starter code notebook and modify your data to fill a regression function. That is, you'll be generating a regression to find your outcome variable, rather than using a multi-class classifier. The outcome from your regression model will fall into a discrete category that corresponds to the product they are purchasing. This method may or may not prove fruitful; you'll need to design an experiment strategy that evaluates this.



*References*

* In Python: https://www.datacamp.com/community/tutorials/recommender-systems-python
* Intuitively: https://www.analyticsvidhya.com/blog/2018/01/factorization-machines/ 
* Formally: https://www.csie.ntu.edu.tw/~b97053/paper/Rendle2010FM.pdf 

