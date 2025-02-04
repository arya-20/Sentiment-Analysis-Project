import pytest
from unittest.mock import patch, MagicMock
import streamlit as st
from security import login
#tests if login function sets logged_in session state correctly

def test_login_page_success():
    """Test that the login function successfully logs in a user."""
    st.session_state.clear()
    st.session_state['auth_mode'] = 'login'
    st.session_state['logged_in'] = False

    with patch('streamlit.text_input', side_effect=["test@example.com", "password"]) as mock_text_input, \
        patch('streamlit.button', return_value=True) as mock_button, \
        patch('firebase_admin.auth.get_user_by_email', return_value=MagicMock(email="test@example.com")) as mock_get_user, \
        patch('security.login.verify_password', return_value={"idToken": "fake_token"}) as mock_verify:
        
        login.login()
    
    assert st.session_state['logged_in'] is True, "User should be logged in on successful login"
    mock_get_user.assert_called_once_with("test@example.com")
    mock_verify.assert_called_once_with("test@example.com", "password")


def test_signup_page_success():
    """Test that the sign-up function successfully creates a new user."""
    st.session_state.clear()
    st.session_state['auth_mode'] = 'signup'
    st.session_state['logged_in'] = False

    with patch('streamlit.text_input', side_effect=["test@example.com", "password123", "password123"]) as mock_text_input, \
        patch('streamlit.button', return_value=True) as mock_button, \
        patch('firebase_admin.auth.create_user', return_value=MagicMock(email="test@example.com")) as mock_create_user:
        
        login.login()
    
    assert st.session_state['logged_in'] is True, "User should be logged in after successful sign-up"
    mock_create_user.assert_called_once_with(email="test@example.com", password="password123")
