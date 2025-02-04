import pytest
import pandas as pd
import streamlit as st
from unittest.mock import MagicMock
from app.screens import dashboard

class MessageCapture:
    error_message = ""
    pyplot_called = False

def test_error(msg):
    MessageCapture.error_message = msg

def test_pyplot(*args, **kwargs):
    MessageCapture.pyplot_called = True

def test_analyze_sentiment():
    return pd.DataFrame({"Sentiment Label": ["Positive", "Neutral", "Negative", "Very Negative"]})

def test_dashboard_success(monkeypatch):
    monkeypatch.setattr(dashboard, "analyze_sentiment", test_analyze_sentiment)
    monkeypatch.setattr(st, "pyplot", test_pyplot)
    monkeypatch.setattr(st, "error", test_error)

    MessageCapture.error_message = ""
    MessageCapture.pyplot_called = False

    dashboard.display()

    assert MessageCapture.pyplot_called, "Dashboard should call st.pyplot for the bar chart"
    assert MessageCapture.error_message == "", "No error should be displayed for successful dashboard display"

def test_dashboard_file_not_found(monkeypatch):
    def raise_file_not_found(*args, **kwargs):
        raise FileNotFoundError("Test: file not found")

    monkeypatch.setattr(dashboard, "analyze_sentiment", raise_file_not_found)
    monkeypatch.setattr(st, "error", test_error)

    MessageCapture.error_message = ""

    dashboard.display()

    assert "cleaned reviews file was not found" in MessageCapture.error_message.lower()
