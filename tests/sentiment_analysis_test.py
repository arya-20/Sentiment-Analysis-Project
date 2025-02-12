import pytest
import pandas as pd
from unittest.mock import patch
from processing.sentiment_analysis import analyze_sentiment

#sample data for test
mock_data = pd.DataFrame({
    "Text": [
        "This product is amazing! I love it!",  #expected: Positive
        "It's okay, not the best but not bad.",  #expected: Neutral
        "Terrible experience, worst product, i hate it.",  #expected: very negative
        "product is pretty bad, quality feels cheap",  #expected: negative
    ]
})

expected_sentiments = ["Positive", "Neutral", "Very Negative", "Negative"]

#mock pandas.read_csv to return mock_data instead of reading from a file
@patch("pandas.read_csv")
def test_analyze_sentiment(mock_read_csv):
    """Test sentiment analysis function with mocked CSV data."""
    mock_read_csv.return_value = mock_data  #set the mock return value to simulate reading from a CSV file

    #run function under test
    df = analyze_sentiment()
    print(df[["Text", "Sentiment", "Sentiment Label"]])

    #assertions verifying behaviour
    assert "Sentiment Label" in df.columns
    assert list(df["Sentiment Label"]) == expected_sentiments
    assert len(df) == len(mock_data)
