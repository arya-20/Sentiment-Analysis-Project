import streamlit as st
@st.cache_resource

def custom_css():
    st.markdown(
        """
        <style>
        /* Background color for the main content */
        .main {
            background-color: #f0f2f6;
        }

        /* Sidebar styling */
        .css-1d391kg {
            background-color: #6A0DAD;
            color: #FFFFFF;
        }

        /* Sidebar header styling */
        .css-1d391kg h1 {
            color: #FFFFFF;
        }


        </style>
        """,
        unsafe_allow_html=True,
    )
