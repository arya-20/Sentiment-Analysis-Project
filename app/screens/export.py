import io
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from processing.sentiment_analysis import analyze_sentiment



def display ():
        df = analyze_sentiment()
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download Analysis Results",
            data=csv,
            file_name="sentiment_analysis_results.csv",
            mime="text/csv",
        )

def get_chart_image():
    df = analyze_sentiment()
    label_counts = df["Sentiment Label"].value_counts()
    fig, ax = plt.subplots()
    label_counts.plot(kind="bar", color=["purple", "purple", "purple", "purple"], ax=ax)

    ax.set_title("Distribution of Sentiment Labels")
    ax.set_xlabel("Sentiment Labels")
    ax.set_ylabel("Frequency")
    
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    return buf

def display_export_page():
    st.title("Export Page")
    st.download_button(
        label="Download Bar Chart as PNG",
        data=get_chart_image(),
        file_name="sentiment_chart.png",
        mime="image/png"
    )