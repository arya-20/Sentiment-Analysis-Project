import streamlit as st

def apply_custom_styles():
    st.markdown(
        """
        <style>

        [data-testid="stSidebar"] {
            background-color: #6300a9 !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

def display_logo():
    st.sidebar.image("BTlogo.png", width=100)
