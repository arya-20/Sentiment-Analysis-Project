import pandas as pd

def process_file(file):

    df = pd.read_csv(file) #read csv file into pandas dataframe
    df.columns = df.columns.str.strip()
    df = df[["Rating", "Title", "Text", "ASIN", "User ID"]]

    return df
