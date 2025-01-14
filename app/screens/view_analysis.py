import streamlit as st
import pandas as pd
from processing.sentiment_analysis import analyze_sentiment

def display():
    st.title("View Analysis")
    st.subheader("Sentiment Analysis Results")
    
    try:
        df = analyze_sentiment()
        
        st.write("Preview of Sentiment Analysis Results:")
        st.dataframe(df.head(10)) 
        
        # Download Option
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download Analysis Results",
            data=csv,
            file_name="sentiment_analysis_results.csv",
            mime="text/csv",
        )
    except FileNotFoundError:
        st.error("The cleaned reviews file was not found. Please upload data first.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
