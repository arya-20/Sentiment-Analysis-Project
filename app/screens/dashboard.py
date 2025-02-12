import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from processing.sentiment_analysis import analyze_sentiment


def display():
    st.title("Dashboard")
    st.subheader("Sentiment Analysis Summary")
    try:
        df = analyze_sentiment()      #uses function from processing/sentiment_analysis
        label_counts = df["Sentiment Label"].value_counts()    #counts the assigned sentiment labels to plot a graph
        fig, ax = plt.subplots()                             #creates a figure and axis to plot the graph
        label_counts.plot(kind="bar", color=["#6300a9"], ax=ax)

        ax.set_title("Distribution of Sentiment Labels")  #titles
        ax.set_xlabel("Sentiment Labels")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    except FileNotFoundError:
        st.error("The cleaned reviews file was not found. Please upload data first.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
