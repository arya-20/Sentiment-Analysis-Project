import pandas as pd

def process_file(file):
    # Load and clean data
    df = pd.read_csv(file, header=None)
    df.columns = ["Rating", "Misc1", "Title", "Text"]
    df = df[["Rating", "Title", "Text"]]
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.columns = [col.strip().title() for col in df.columns]
    return df