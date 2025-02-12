import io
import pytest
import streamlit as st
from app.screens.upload import display

#utility class to capture streamlit messages
class MessageCapture:
    message = ""

#these functions capture different message types in Streamlit
def _capture_success(msg):
    MessageCapture.message = msg

def _capture_info(msg):
    MessageCapture.message = msg

def _capture_error(msg):
    MessageCapture.message = msg

#simulating no file being uploaded
def test_file_uploader_no_file(*args, **kwargs):
    return None

def test_file_uploader_valid_file(*args, **kwargs):
    return io.StringIO("Rating,Title,Text,ASIN,User ID\nGreat Product!,Really good quality,B00123,User001")

#applying the Streamlit monkeypatch for capturing messages
@pytest.fixture(autouse=True)
def patch_st(monkeypatch):
    """Patch Streamlit's success, error, and info functions to capture messages."""
    monkeypatch.setattr(st, "success", _capture_success)
    monkeypatch.setattr(st, "error", _capture_error)
    monkeypatch.setattr(st, "info", _capture_info)

#test case - no file is uploaded
def test_upload_no_file(monkeypatch):
    """Test that the UI prompts users to upload a file when no file is provided."""
    monkeypatch.setattr(st, "file_uploader", test_file_uploader_no_file)
    MessageCapture.message = ""  #reset captured message

    display()  #run the upload screen logic

    assert "Upload a CSV file" in MessageCapture.message, "Expected prompt message when no file is uploaded."

#test case - valid file upload
def test_upload_valid_file(monkeypatch):
    """Test that the file upload process works correctly when a valid CSV is provided."""
    monkeypatch.setattr(st, "file_uploader", test_file_uploader_valid_file)
    MessageCapture.message = ""  #reset captured message

    display()  #run the upload screen logic

    assert "File uploaded and cleaned successfully!" in MessageCapture.message, "Expected success message after file upload."
