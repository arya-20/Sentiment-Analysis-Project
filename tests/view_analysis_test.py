import pytest
import pandas as pd
import urllib.parse
from unittest.mock import patch
import streamlit as st

def test_analyze_sentiment():
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
    monkeypatch.setattr("processing.sentiment_analysis.analyze_sentiment", test_analyze_sentiment)   #patch analyze_sentiment to return data


    fake_options = [
        "Review 1: Great product, loved it!...",
        "Review 2: It's okay, average quality....",
        "Review 3: Terrible experience, will never buy again...."
    ]
    
    monkeypatch.setattr(st, "selectbox", lambda label, options: fake_options[2])     #patch select box and select reivew
    monkeypatch.setattr(st, "button", lambda label, key=None: True if label == "Generate Auto-Response" else False)
    
    markdown_calls = []
    def test_markdown(value, unsafe_allow_html=False):
        markdown_calls.append(value)
    monkeypatch.setattr(st, "markdown", test_markdown)

    dataframe_displayed = []
    def test_data_frame(df):
        dataframe_displayed.append(df)
    monkeypatch.setattr(st, "dataframe", test_data_frame)
    
    #now import and call the display function from view_analysis
    from app.screens import view_analysis
    view_analysis.display()
    
    assert len(dataframe_displayed) > 0, "Dataframe was not displayed"
    displayed_df = dataframe_displayed[0]
    assert displayed_df.shape == (3, 3), "Expected dataframe to have 3 rows and 3 columns"
    assert list(displayed_df.columns) == ["Rating", "Text", "Sentiment Label"], "Dataframe columns do not match the expected ones"
    assert any("mailto:" in call for call in markdown_calls), "Expected a mailto link in st.markdown output"      #Check at least one markdown call contains "mailto:" in it
