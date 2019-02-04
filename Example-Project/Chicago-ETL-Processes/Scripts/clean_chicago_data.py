import pandas as pd

def main(f_name):
    
    df = pd.read_csv(f_name, index_col = "ID")
    
    # keep a subset of columns
    keep_list = ["Case Number", "Date", "Block", "Primary Type", "Description", "Location Description", "Arrest", "Year", "Location"]
    reduced_df = df[keep_list]

    # drop rows that are missing Location Description
    df = df[ (df["Location Description"]).isna() == False ]
    
    # drop rows that are missing Location, geo coordinates
    df = df[ (df["Location"]).isna() == False ]
    
    # write to disk
    df.to_csv("../crimes_2018_reduced.csv")
    

if __name__ == "__main__":

    main("../Data/crimes_2018.csv")
    