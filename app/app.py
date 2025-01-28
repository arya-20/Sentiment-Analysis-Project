import os
import sys

# Add project root to system path for imports
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

import streamlit as st
from styling import custom_css
from screens import dashboard, upload, view_analysis, export
from security.login import login  # Import the updated login function

custom_css()

# Initialize session state for login status
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Check if the user is logged in
if not st.session_state['logged_in']:
    login()  # Show login/signup page if not logged in
else:
    # Sidebar Navigation
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Go to", ["Dashboard", "Upload Data", "View Analysis", "Export Data"])

    # Page routing
    if page == "Dashboard":
        dashboard.display()
    elif page == "Upload Data":
        upload.display()
    elif page == "View Analysis":
        view_analysis.display()
    elif page == "Export Data":
        export.display()
