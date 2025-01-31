import pandas as pd
from processing.file_handler import process_file
from io import StringIO

def test_process_file():
    sample_data = "5,Misc,Great product!,Loved it!\n3,Misc,Okay,Average quality."
    file = StringIO(sample_data)  # Simulating file upload
    df = process_file(file)
    
    assert df.shape[1] == 3  #check column count
    assert "Rating" in df.columns
    assert df.iloc[0]["Text"] == "Loved it!"
