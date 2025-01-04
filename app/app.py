import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.append(project_root)


import streamlit as st
from screens import dashboard, upload, view_analysis, export

# Sidebar Nav
st.sidebar.title("Menu")
page = st.sidebar.radio("Go to", ["Dashboard", "Upload Data", "View Analysis", "Export Data"])

if page == "Dashboard":
    dashboard.display()
elif page == "Upload Data":
    upload.display()
elif page == "View Analysis":
    view_analysis.display()
elif page == "Export Data":
    export.display()
