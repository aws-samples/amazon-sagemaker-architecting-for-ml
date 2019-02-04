# Updated Project Goal

Linear learner worked functionally, but it was not highly accurate. Next iteration:

1. Use ETL to add:
      - time of day, analyze, does it impact?
      - month, analyze, does it impact? 
      - is_precipitation 
      - is_hot
      - increase in temperature from yesterday
      - crimes-to-date on that block 
      - need to find out the patterns of crime by day, what are the spikes / troughs?
      - add total count of crimes on that block per week, per year, total number of homocides ever
      - add week's worth of events for a single day's prediction

2. Use Obj2Vec to create embeddings
      - Each block & feature vector should have its own embedding
      - We can just grab all the crime in each block for the past week, then feed that as unequal size arrays into Obj2Vec to get embeddings.

3. Use Factorization Machines
      - Generate a matrix of all blocks against all types of crime
      - Actually want to train on sequence of criminal activity on that block. 
            - In which case a single query would be a week's worth of activity on that block, for crimes the next day. 

4. Run KNN
      - Build a similarity engine 
      - Run queries to find blocks with high crime likelihood

5. Put into a heat map 
      - Use Folium
      - Extend with an SMS subscription service:
        - If there's likely to be a crime on your block, get a notification

## References
* https://arxiv.org/pdf/1806.01486.pdf 
