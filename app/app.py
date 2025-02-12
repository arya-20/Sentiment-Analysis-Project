import os
import sys
import streamlit as st
from styling import apply_custom_styles, display_logo
apply_custom_styles()
display_logo()


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

from screens import dashboard, upload, view_analysis, detailed_analysis, export
from security.login import login  # import the updated login function


if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:  #check if the user is logged in

    login()  #show login/signup page if not logged in
else:
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Go to", ["Upload Data", "Dashboard", "View Analysis","Detailed Analysis", "Export Data"])

    if page == "Upload Data":
        upload.display()
    elif page == "Dashboard":
        dashboard.display()
    elif page == "View Analysis":
        view_analysis.display()
    elif page == "Detailed Analysis":
        detailed_analysis.display()
    elif page == "Export Data":
        export.display()
