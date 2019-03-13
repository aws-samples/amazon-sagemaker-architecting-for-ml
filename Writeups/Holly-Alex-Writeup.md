
##Title: Books on Tape - Author Classification from Dante and Shakespeare

Given a line from either Shakespeare or Dante, we will train a machine learning model that will accurately predict the author. 

We will investigate three candidate models and compare their performance: Amazon’s BlazingText, Naive Bayes, and KNeighbors.

We have chosen two scenes from the Merchant of Venice by William Shakespeare and two scenes from the Divine Comedy by Dante Alighieri. These scenes will be transcribed using Amazon Transcribe. Word transcription data will then be processed and cleaned. Transcriptions with low confidence will be evaluated for removal. Data will then be explored and formatted. 

Formatted data will be used to train models and features selected. A second set of data will be chosen for and processed for validation. Each model’s performance will be evaluated and compared. 



**Questions we are now considering/ Interesting thoughts**
1. How well can Amazon Transcribe transcribe the unique language of Shakespeare? Will transcriptions with low confidence turn out to be revealing language for classifying authors?
2. Shakespeare is written in iambic pentameter. Dante is originally written in Terza Rima and often translated into iambic pentameter. Is meter a revealing feature for author classification?  Can meter be used as a feature?
3. Features of interest - words common by one author or another; uniqueness as a feature; clusters of words; semantics as a feature - Dante will have a lot of “fiery, hell, burning” 


**Process**
1. Transcription - How are data points subsetted? How do we feed in separate data points to transcription? Before? After? 
2. Data cleaned and formatted - What points are we throwing out? Confidence threshold? How are we formatting data?
3. How do we explore data? Confusion matrix? Lots of histograms?
4. Feature selection
5. First model trainings
6. Model choice
7. Model optimization/feature selection/hypertuning
8. Validation
9. Presentation