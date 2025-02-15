import pytest
import pandas as pd
import urllib.parse
from unittest.mock import patch
import streamlit as st

def test_analyze_sentiment():
    #mock sentiment analysis function with test data
    data = {
        "Rating": [5, 3, 1],
        "Text": [
            "Great product, loved it!",
            "It's okay, average quality.",
            "Terrible experience, will never buy again."
        ],
        "Sentiment Label": ["Positive", "Neutral", "Negative"]
    }
    return pd.DataFrame(data)

def test_view_analysis_generate_auto_response(monkeypatch):
    #patch analyze_sentiment function to return mock data
    monkeypatch.setattr("processing.sentiment_analysis.analyze_sentiment", test_analyze_sentiment)

    #mocking user selection with fake options
    fake_options = [
        "Review 1: Great product, loved it!...",
        "Review 2: It's okay, average quality....",
        "Review 3: Terrible experience, will never buy again...."
    ]
    
    monkeypatch.setattr(st, "selectbox", lambda label, options: fake_options[2])     
    monkeypatch.setattr(st, "button", lambda label, key=None: True if label == "Generate Auto-Response" else False)
    
    #capture calls to st.markdown to check if the mailto link is generated
    markdown_calls = []
    def test_markdown(value, unsafe_allow_html=False):
        markdown_calls.append(value)
    monkeypatch.setattr(st, "markdown", test_markdown)

    #capture calls to st.dataframe to check if the DataFrame is displayed
    dataframe_displayed = []
    def test_data_frame(df):
        dataframe_displayed.append(df)
    monkeypatch.setattr(st, "dataframe", test_data_frame)
    
    #import and call the display function from view_analysis
    from app.screens import view_analysis
    view_analysis.display()
    
    #ensure the DataFrame was displayed
    assert len(dataframe_displayed) > 0, "Dataframe was not displayed"
    displayed_df = dataframe_displayed[0]
    
    #validate the DataFrame structure (3 rows, 3 columns)
    assert displayed_df.shape == (3, 3), "Expected dataframe to have 3 rows and 3 columns"
    assert list(displayed_df.columns) == ["Rating", "Text", "Sentiment Label"], "Dataframe columns do not match the expected ones"
    
    #Ensure an email link ("mailto:") was generated in the markdown output
    assert any("mailto:" in call for call in markdown_calls), "Expected a mailto link in st.markdown output"
