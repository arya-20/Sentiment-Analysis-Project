import pytest
from unittest.mock import patch, MagicMock
import streamlit as st
from security import login

#tests if login function sets logged_in session state correctly

def test_login_page_success():
    """Test that the login function successfully logs in a user."""

    #clear session state and set initial values
    st.session_state.clear()
    st.session_state['auth_mode'] = 'login'
    st.session_state['logged_in'] = False

    #mocks user inputs and Firebase authentication responses
    with patch('streamlit.text_input', side_effect=["test@example.com", "password"]) as mock_text_input, \
        patch('streamlit.button', return_value=True) as mock_button, \
        patch('firebase_admin.auth.get_user_by_email', return_value=MagicMock(email="test@example.com")) as mock_get_user, \
        patch('security.login.verify_password', return_value={"idToken": "fake_token"}) as mock_verify:
        
        login.login() #calling the login function
    
    #assertions to check expected behaviour
    assert st.session_state['logged_in'] is True, "User should be logged in on successful login"
    mock_get_user.assert_called_once_with("test@example.com")
    mock_verify.assert_called_once_with("test@example.com", "password")


#test if failed login attempts are handled properly 
def test_login_page_failure():
    """Test that the login function handles incorrect credentials correctly."""

    #clear session state
    st.session_state.clear()
    st.session_state['auth_mode'] = 'login'
    st.session_state['logged_in'] = False

    #attempt incorrect login attempt
    with patch('streamlit.text_input', side_effect=["wrong@example.com", "wrongpassword"]) as mock_text_input, \
        patch('streamlit.button', return_value=True) as mock_button, \
        patch('firebase_admin.auth.get_user_by_email', return_value=MagicMock(email="wrong@example.com")) as mock_get_user, \
        patch('security.login.verify_password', side_effect=ValueError("INVALID_PASSWORD")) as mock_verify:
        
        login.login()
    
    #ensure user does not get access
    assert st.session_state['logged_in'] is False, "User should not be logged in with incorrect credentials"
    mock_get_user.assert_called_once_with("wrong@example.com")
    mock_verify.assert_called_once_with("wrong@example.com", "wrongpassword")
    


#test if signup functions as expected
def test_signup_page_success():
    """Test that the sign-up function successfully creates a new user."""
    st.session_state.clear()
    st.session_state['auth_mode'] = 'signup'
    st.session_state['logged_in'] = False

#mock user input
    with patch('streamlit.text_input', side_effect=["test@example.com", "password123", "password123"]) as mock_text_input, \
        patch('streamlit.button', return_value=True) as mock_button, \
        patch('firebase_admin.auth.create_user', return_value=MagicMock(email="test@example.com")) as mock_create_user:
        
        login.login()
    
    #assertions checking if new user is created and logged in
    assert st.session_state['logged_in'] is True, "User should be logged in after successful sign-up"
    mock_create_user.assert_called_once_with(email="test@example.com", password="password123")