import pytest
import pandas as pd
import streamlit as st
from unittest.mock import patch

def test_analyze_sentiment(): #dummy data 
    return pd.DataFrame({
        "Rating": [5, 3, 1, 2],
        "Title": ["Title1", "Title2", "Title3", "Title4"],
        "Text": [
            "Great product, loved it!",
            "Okay product, average quality.",
            "Terrible product, will never buy again.",
            "Not good, could be better."
        ],
        "Sentiment Label": ["Positive", "Neutral", "Very Negative", "Negative"],
        "ASIN": ["A123456789", "B123456789", "C123456789", "D123456789"],
        "User ID": ["U1", "U2", "U3", "U4"]
    })

@pytest.fixture
def setup_mocks(monkeypatch):
    monkeypatch.setattr("processing.sentiment_analysis.analyze_sentiment", test_analyze_sentiment)
    
    m_dataframe = patch.object(st, "dataframe").start()
    
    write_calls = []
    def fake_write(*args, **kwargs):
        write_calls.append(" ".join(str(arg) for arg in args))
    monkeypatch.setattr(st, "write", fake_write)
    
    m_text_input = patch.object(st, "text_input").start()
    m_text_input.side_effect = lambda label, **kwargs: label
    
    yield m_dataframe, write_calls, m_text_input
    patch.stopall()

def test_detailed_analysis_ui(setup_mocks, monkeypatch):
    m_dataframe, write_calls, m_text_input = setup_mocks

    from app.screens import detailed_analysis
    detailed_analysis.display()

    assert m_dataframe.call_count == 1, f"Expected 1 call to st.dataframe, got {m_dataframe.call_count}"
    found_negative_header = any("Most Negative Reviews" in call for call in write_calls)
    assert found_negative_header, "Expected 'Most Negative Reviews' header to be displayed via st.write."
    assert m_text_input.call_count == 2, f"Expected 2 calls to st.text_input, got {m_text_input.call_count}"