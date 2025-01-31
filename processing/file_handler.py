import pandas as pd

def process_file(file):
    df = pd.read_csv(file)

    df.columns = df.columns.str.strip()

    df = df[["Rating", "Title", "Text", "ASIN", "User ID"]]

    return df
