import streamlit as st
import pandas as pd
from processing.sentiment_analysis import analyze_sentiment

def display():
    st.title("View Analysis")
    st.subheader("Sentiment Analysis Results")
    
    try:
        df = analyze_sentiment()

        # Display general statistics based on the DataFrame
        st.write(f"Total number of reviews: {df.shape[0]}")
        st.write(f"Number of unique ASINs: {df['ASIN'].nunique()}")
        st.write(f"Number of unique User IDs: {df['User ID'].nunique()}")
#        st.write(f"Average Rating: {df['Rating'].mean()}")

        st.write("Preview of Sentiment Analysis Results:")
        st.dataframe(df)

    except FileNotFoundError:
        st.error("The cleaned reviews file was not found. Please upload data first.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
