import pandas as pd

def process_file(uploaded_file):
    # Load and clean data
    df = pd.read_csv(uploaded_file, header=None)
    df.columns = ["Rating", "Misc1", "Title", "Text"]
    df = df[["Rating", "Title", "Text"]]
    return df

