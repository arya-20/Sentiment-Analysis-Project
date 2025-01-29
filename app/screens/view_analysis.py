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
        
        st.subheader("ASIN-Based Sentiment Analysis")
        
        #input field to filter by ASIN
        asin_filter = st.text_input("Enter ASIN to filter (optional):")
        
        if asin_filter:
            filtered_df = df[df["Asin"] == asin_filter]
            
            if filtered_df.empty:
                st.warning(f"No reviews found for ASIN: {asin_filter}")
            else:
                st.write(f"Sentiment Analysis for ASIN: {asin_filter}")
                st.dataframe(filtered_df[["Asin", "Text", "Sentiment Label", "Sentiment"]])
                
                #chart sentiment distribution for the filtered ASIN
                st.subheader(f"Sentiment Distribution for ASIN: {asin_filter}")
                sentiment_counts = filtered_df["Sentiment Label"].value_counts()
                
                fig, ax = plt.subplots()
                sentiment_counts.plot(kind="bar", color="purple", ax=ax)
                ax.set_title(f"Sentiment Distribution for ASIN: {asin_filter}")
                ax.set_xlabel("Sentiment Labels")
                ax.set_ylabel("Frequency")
                st.pyplot(fig)
        else:
            st.info("Enter an ASIN to see specific sentiment analysis.")

            st.subheader("Most Critical - Urgent Action Needed")
        critical_reviews = df[df["Sentiment"] <= -0.5]
        if critical_reviews.empty:
            st.write("No reviews with 'Very Negative' sentiment found.")
        else:
            st.write("Below are reviews with 'Very Negative' sentiment (Sentiment Score ≤ -0.5):")
            st.dataframe(critical_reviews[[ "Text", "Sentiment Label", "Sentiment"]])
            
    except FileNotFoundError:
        st.error("The cleaned reviews file was not found. Please upload data first.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
