import streamlit as st
import pandas as pd
from processing.file_handler import process_file  

def display():
    st.title("Upload and View Data")
    uploaded_file = st.file_uploader("Choose a CSV file to upload", type="csv")
    
    if uploaded_file:
        try:
            cleaned_df = process_file(uploaded_file)
            cleaned_df.to_csv("data/review_file.csv", index=False)

            st.success("File uploaded and cleaned successfully!")

        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")
    else:
        st.info("Upload a CSV file to get started.")
