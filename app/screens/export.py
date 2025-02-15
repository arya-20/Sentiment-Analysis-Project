import io
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from processing.sentiment_analysis import analyze_sentiment



def display ():
        st.title("Download Analysis Results")
        df = analyze_sentiment()
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download",
            data=csv,
            file_name="sentiment_analysis_results.csv",
            mime="text/csv",
        )