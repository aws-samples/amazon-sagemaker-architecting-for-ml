# Books On Tape: Author Classification

**Introduction**
Literary authors have a wide variety of styles, contexts, and characters they describe in their works. Many of these styles are repeatable, demonstrating identifiable patterns across their bodies of work. These styles can evolve over time, changing as the lives of the authors themselves evolve. 

**Project Goals**
Your mission is two-fold. First, you will use Amazon Transcribe to generate text files from books on tape recordings. Second, you will use those text files to build a machine learning model that can recognize the difference between two different authors at similar points in historical time: Jane Austen and Charles Dickens. 

**Data sources**
There are many sources of literature in the public domain, and books that are recorded for free usage. Here is one option: 
-http://www.openculture.com/freeaudiobooks 

Download two audio files, one from both Jane Austen and Charles Dickens. Make sure to select MP3 formats, because you will run a Transcribe job with those files. For now, select only one file. You'll break this into your train and validation sets. When you're ready to test your final model, you'll download an additional book from both authors, run it against your models, and attempt to get an accurate prediction. 

Store these downloads in an S3 bucket that your team has access to. 

**Machine Learning Method**
For classification, there are a wide variety of options available to you. The easiest way to get started in text classification is using the SageMaker built-in algorithm, BlazingText. For a deeper dive on BlazingText, make sure to read the SageMaker documentation's introduction to the algorithm, specifically the 'How it works' section. 

 When you get responses from the Transcribe job, you will need to determine what length of document you use to train the model. This means that you will need to format the Transcribe results into a both data type that BlazingText can read, and a data type that intuitively lends itself well to the author classification problem. You might do this sentence-by-sentence. You also might do this chapter-by-chapter. Make your selection first for ease-of-use, and as your project develops enhance your feature engineering strategy as necessary.

**Presenting Results**
In particular, we are most interested in understanding which of your methods lead to the best model performance. How will you evaluate your model? Does a larger variety of data lead to a better model, or does a different feature engineering strategy? How would you deploy this into production, and what would your entire architecture look like? 




