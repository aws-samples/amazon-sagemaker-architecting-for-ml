import pandas as pd


def get_station_keep_list(df):
    s = df["NAME"].value_counts().to_dict()

    keep_stations = {}

    for k, v in s.items():
        if v > 200:
            keep_stations[k] = v
            
    return list(keep_stations.keys())



def main(f_name):
    
    df = pd.read_csv(f_name, index_col = "STATION")
    
    # Drop uneccessary columns
    keep_list = ["NAME", "LATITUDE", "LONGITUDE", "DATE", "TMAX", "TMIN"]
    reduced_df = df[keep_list]
    
    station_keep_list = get_station_keep_list(reduced_df)
    
    final_df = reduced_df[ df["NAME"].isin(station_keep_list)]
    
    
    final_df.to_csv("../Data/cleaned_weather_2018.csv")
    

if __name__ == "__main__":
    main("../Data/weather_2018.csv")
    
    
    
    