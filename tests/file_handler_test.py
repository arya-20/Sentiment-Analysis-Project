import pandas as pd
import pytest
from io import StringIO
from processing.file_handler import process_file  

@pytest.fixture  #fixture to set up mocks
def sample_csv():
    """Create a sample CSV file as a string."""
    data = """Rating, Title ,Text, ASIN, User ID, ExtraColumn
5, "Great Product", "I love it!", B001, U123, ExtraData
3, "Average", "It's okay.", B002, U124, ExtraData
1, "Terrible", "Worst purchase ever.", B003, U125, ExtraData
"""
    return StringIO(data)  #simulates a file object

def test_process_file(sample_csv):
    """Test if process_file correctly processes CSV data."""
    df = process_file(sample_csv)

    #check if expected columns exist
    expected_columns = ["Rating", "Title", "Text", "ASIN", "User ID"]
    assert list(df.columns) == expected_columns, "Processed DataFrame has incorrect columns"
    assert "ExtraColumn" not in df.columns, "Extra columns should be removed"
