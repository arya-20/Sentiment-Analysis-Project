import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from processing.sentiment_analysis import analyze_sentiment


def display():
    st.title("Dashboard")
    st.subheader("Sentiment Analysis Summary")
    try:
        df = analyze_sentiment()
        label_counts = df["Sentiment Label"].value_counts()
        fig, ax = plt.subplots()
        label_counts.plot(kind="bar", color=["#6300a9"], ax=ax)

        ax.set_title("Distribution of Sentiment Labels")
        ax.set_xlabel("Sentiment Labels")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    except FileNotFoundError:
        st.error("The cleaned reviews file was not found. Please upload data first.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
