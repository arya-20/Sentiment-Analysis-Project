import pytest
import pandas as pd
import streamlit as st
from unittest.mock import MagicMock
from app.screens import dashboard

#utility class captures error messages and check if pyplot was called
class MessageCapture:
    error_message = ""
    pyplot_called = False

#function to capture error message
def capture_error(msg):
    MessageCapture.error_message = msg

#function to track when st.pyplot() is called
def test_pyplot(*args, **kwargs):
    MessageCapture.pyplot_called = True

#mock function to simulate sentiment analysis output
def test_analyze_sentiment():
    return pd.DataFrame({"Sentiment Label": ["Positive", "Neutral", "Negative", "Very Negative"]})

#test case - successful dashboard display
def test_dashboard_success(monkeypatch):

    #replace functions with test functions
    monkeypatch.setattr(dashboard, "analyze_sentiment", test_analyze_sentiment)
    monkeypatch.setattr(st, "pyplot", test_pyplot)
    monkeypatch.setattr(st, "error", capture_error)

    MessageCapture.error_message = ""
    MessageCapture.pyplot_called = False

    dashboard.display()

    #verify graph was rendered
    assert MessageCapture.pyplot_called, "Dashboard should call st.pyplot for the bar chart"
    assert MessageCapture.error_message == "", "No error should be displayed for successful dashboard display"


#Test case - for handling missing file error
def test_dashboard_file_not_found(monkeypatch):
    def raise_file_not_found(*args, **kwargs):
        raise FileNotFoundError("Test: file not found")

#replace functions with test functions
    monkeypatch.setattr(dashboard, "analyze_sentiment", raise_file_not_found)
    monkeypatch.setattr(st, "error", capture_error)

    MessageCapture.error_message = ""

    dashboard.display()

    assert "cleaned reviews file was not found" in MessageCapture.error_message.lower()
