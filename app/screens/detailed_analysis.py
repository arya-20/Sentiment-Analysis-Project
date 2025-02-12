import streamlit as st
import pandas as pd
from processing.sentiment_analysis import analyze_sentiment

def display ():
    st.title("Detailed Sentiment Analysis")

    df = analyze_sentiment()

    st.subheader("More Details of Reviews")
    st.dataframe(df)   #show the whole dataframe with all the details


    st.write("### Most Negative Reviews")   #filter for "Very Negative" reviews and show first 20
    negative_reviews = df[df["Sentiment Label"] == "Very Negative"]
    st.write(negative_reviews[["Title", "Text", "ASIN", "User ID"]].head(20))

    asin_filter = st.text_input("Enter ASIN to filter reviews:")  #search filter for ASIN
    if asin_filter:
        filtered_by_asin = df[df["ASIN"] == asin_filter]
        st.write(f"### Reviews for ASIN: {asin_filter}")
        st.write(filtered_by_asin[["Title", "Text", "Sentiment Label"]])

    user_id_filter = st.text_input("Enter User ID to filter reviews:")   #search filter for user ID
    if user_id_filter:
        filtered_by_user = df[df["User ID"] == user_id_filter]
        st.write(f"### Reviews by User ID: {user_id_filter}")
        st.write(filtered_by_user[["Title", "Text", "Sentiment Label"]])

