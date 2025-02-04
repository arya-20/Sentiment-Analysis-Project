import io
import pytest
import streamlit as st
from app.screens.upload import display

class MessageCapture:
    message = ""

def _capture_success(msg):
    MessageCapture.message = msg

def _capture_info(msg):
    MessageCapture.message = msg

def _capture_error(msg):
    MessageCapture.message = msg

def test_file_uploader_no_file(*args, **kwargs):
    return None

def test_file_uploader_valid_file(*args, **kwargs):
    return io.StringIO("Rating,Title,Text,ASIN,User ID\nGreat Product!,Really good quality,B00123,User001")


@pytest.fixture(autouse=True)
def patch_st(monkeypatch):
    monkeypatch.setattr(st, "success", _capture_success)
    monkeypatch.setattr(st, "error", _capture_error)
    monkeypatch.setattr(st, "info", _capture_info)

def test_upload_no_file(monkeypatch):
    monkeypatch.setattr(st, "file_uploader", test_file_uploader_no_file)
    MessageCapture.message = ""

    display()

    assert "Upload a CSV file" in MessageCapture.message

def test_upload_valid_file(monkeypatch):
    monkeypatch.setattr(st, "file_uploader", test_file_uploader_valid_file)
    MessageCapture.message = ""

    display()

    assert "File uploaded and cleaned successfully!" in MessageCapture.message
