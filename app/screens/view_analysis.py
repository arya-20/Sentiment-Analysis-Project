import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from processing.sentiment_analysis import analyze_sentiment

def display():
    st.title("View Analysis")
    st.subheader("Sentiment Analysis Results")
    
    try:
        df = analyze_sentiment()
        
        st.write("Preview of Sentiment Analysis Results:")
        st.dataframe(df) 
        
        # Download Option
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download Analysis Results",
            data=csv,
            file_name="sentiment_analysis_results.csv",
            mime="text/csv",
        )
        st.subheader("Sentiment Distribution:")
        label_counts = df["Sentiment Label"].value_counts()

        fig, ax = plt.subplots()
        label_counts.plot(kind="bar", color=["purple", "purple", "purple", "purple"], ax=ax)
        ax.set_title("Distribution of Sentiment Labels")
        ax.set_xlabel("Sentiment Labels")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    except FileNotFoundError:
        st.error("The cleaned reviews file was not found. Please upload data first.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
