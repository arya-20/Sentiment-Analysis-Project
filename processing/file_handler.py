import pandas as pd
import re

def extract_asin(text):
    """Extract ASIN from the review text."""
    match = re.search(r'\b[A-Z0-9]{10}\b', text) #regexp
    return match.group(0) if match else None

def process_file(file):
    # Load and clean data
    df = pd.read_csv(file, header=None)
    df.columns = ["Rating", "Misc1", "Title", "Text"]
    df = df[["Rating", "Title", "Text"]]
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.columns = [col.strip().title() for col in df.columns]
    return df