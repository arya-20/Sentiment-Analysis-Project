import os
import sys
import requests
import streamlit as st
from firebase_admin import auth, initialize_app, credentials

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.append(project_root)


cred = credentials.Certificate("security/firebase_credentials.json")  #initializing firebase with credentials
initialize_app(cred)

FIREBASE_WEB_API_KEY = "AIzaSyAQvSQUFThAPeDj75QTrj7h9OdsloF6jJY" 

def verify_password(email, password):
    """Verify the user's password using Firebase's REST API."""
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_WEB_API_KEY}"
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:     #checking if auth was successfull
        return response.json()
    else:
        raise ValueError(response.json().get("error", {}).get("message", "Authentication failed"))



def login():  #login screen ui
    if 'auth_mode' not in st.session_state:
        st.session_state['auth_mode'] = 'login'  #default to login mode

    st.title("BT Feedback - Sentiment Analyser")
    
    if st.session_state['auth_mode'] == 'login':  #toggle between login and signup
        st.subheader("Login")

        email = st.text_input("Email")    #input fields
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            try:
                user = auth.get_user_by_email(email)   #retrieve user data from firebase
                verify_password(email, password)       #verify password using firebase rest api
                
                st.session_state['logged_in'] = True   #mark session state as logged in
                st.success(f"Welcome, {user.email}!")
            except Exception as e:
                st.error(f"Login failed: {str(e)}")
        
        if st.button("Go to Sign Up"):
            st.session_state['auth_mode'] = 'signup'   #button switches to signup 



    elif st.session_state['auth_mode'] == 'signup':
        st.subheader("Sign Up")

        email = st.text_input("Email for Sign Up", key="signup_email")      #input fields for singing up
        password = st.text_input("Password for Sign Up", type="password", key="signup_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
    
        if st.button("Sign Up", key="signup_button"):
            if password != confirm_password:
                st.error("Passwords do not match. Please try again.")
            else:
                try:
                    user = auth.create_user(email=email, password=password)   #create new user in firebase authentication
                    st.session_state['logged_in'] = True
                    st.success(f"Account created successfully for {user.email}!")
                except Exception as e:
                    st.error(f"Sign Up failed: {str(e)}")
        
        if st.button("Go to Login"):
            st.session_state['auth_mode'] = 'login'
