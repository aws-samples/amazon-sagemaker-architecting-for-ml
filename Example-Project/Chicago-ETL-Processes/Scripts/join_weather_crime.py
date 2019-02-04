import pandas as pd
from datetime import date
from dateutil.rrule import rrule, DAILY

def reformat_crime_date(date_string):

    items = date_string.split("/")
    year = items[-1]
    month = items[0]
    day = items[1]    
    
    new_date = "{}-{}-{}".format(year, month, day)
        
    return new_date

def get_mapper(crime_days):

    d = {}

    for each in crime_days:
        old_date = each.split()[0]
        if old_date not in d:
            new_date = reformat_crime_date(old_date[:])
            d[old_date] = new_date

    return d

def get_average_by_day(weather_df, days_in_2018):

    rt = {}
    
    for d in days_in_2018:

        # now, for each day, grab every TMAX
        rows = weather_df.loc[ weather_df["DATE"] == d]
        rt[d] = rows["TMAX"].mean() 
    return rt


def get_mapping_dict():

    rt = {}

    a = date(2018, 1, 1)
    b = date(2018, 9, 30)

    day_of_week = {0: "Monday", 1:"Tuesday", 2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}

    for dt in rrule(DAILY, dtstart=a, until=b):
        day_of_year = dt.strftime("%Y-%m-%d")
        n = dt.weekday()
        day = day_of_week[n]
        rt[day_of_year] = day
        
    return rt

def add_day_of_week(df):

    for idx, row in df.iterrows():
        day_of_year = row["DATE"]
        day_of_week = m[day_of_year]
        df.loc[idx, "Day of Week"] = day_of_week
        
    return df


def get_days_from_range(day_1, day_2):

    rt = []
    
    a = date(day_1[0], day_1[1], day_1[2])
    b = date(day_2[0], day_2[1], day_2[2])

    for dt in rrule(DAILY, dtstart=a, until=b):
        day_of_year = dt.strftime("%Y-%m-%d")
        rt.append(day_of_year)
    return rt


def get_updated_data(weather_file, crime_file):
    
    # read into memory
    weather_df = pd.read_csv(weather_file)
    crime_df = pd.read_csv(crime_file, index_col = "ID")
    
    # add new columns
    weather_df["Day Of Week"] = [" " for i in range(weather_df.shape[0])]    
    crime_df["Reformatted Date"] = [" " for i in range(crime_df.shape[0])]

    # get day of week for weather
    weather_df = add_day_of_week(weather_df)
    
    # compute averages by day
    
    return weather_df, crime_df

def main(weather_file, crime_file):
    '''
    The primary function for execution. This does the following:
        (1) Reads weather and crime data into memory
        (2) Adds a Day of the week to the weather data set
        (3) Builds a mapper to reformat the crime dates
        (4) 

    '''

    weather_df, crime_df = get_updated_data(weather_file, crime_file)

        
    mapper = get_mapper(crime_df["Date"].unique().tolist()[:])

    # get dates in 2018
    days_in_2018 = get_days_from_range([2018, 1, 1], [2018, 9, 30])

    averages = get_average_by_day(weather_df, days_in_2018)

    for idx, row in crime_df.iterrows():

        new_date = mapper[row["Date"].split()[0]]

        crime_df.loc[idx, "Reformatted Date"] = new_date
    
    
main("../Data/cleaned_weather_2018.csv", "../Data/crimes_2018_reduced.csv")
