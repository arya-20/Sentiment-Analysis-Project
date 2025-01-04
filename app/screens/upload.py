import streamlit as st
import pandas as pd

def display():
    st.title("View Data")

    csv_file_path = "data/cleaned_reviews.csv"

    try:
        df = pd.read_csv(csv_file_path)
        st.write("Preview of Data:")
        st.dataframe(df)
    except FileNotFoundError:
        st.error("file was not found")
