import streamlit as st
import pandas as pd
import urllib.parse 
from processing.sentiment_analysis import analyze_sentiment

def generate_auto_response(sentiment, review_text):   #auto response templates 
    if sentiment == "Positive":
        return "Thank you for your positive feedback! We're thrilled to hear that you enjoyed your experience. 😊"
    elif sentiment == "Neutral":
        return "Thank you for sharing your feedback. We appreciate your thoughts and will consider them moving forward."
    elif sentiment == "Negative":
        return "We're sorry to hear about your experience. 😔 We value your feedback and will work to improve. Please reach out if you'd like further assistance."
    else:
        return "We are deeply sorry about your experience. your request has been prioritised and we are working to fix the issue. Please reach out to our team and support will be provided"

def display():
    st.title("View Analysis")
    st.subheader("Sentiment Analysis Results")
    
    try:
        df = analyze_sentiment()

        st.write(f"Total number of reviews:    {len(df)}")
        st.write(f"Average Rating:             {df['Rating'].mean():.2f}")

        selected_columns = df[["Rating", "Text", "Sentiment Label"]]
        st.dataframe(selected_columns)

        review_options = [f"Review {i + 1}: {row['Text'][:50]}..." for i, row in selected_columns.iterrows()]     #dropdown to select review for auto response
        selected_review = st.selectbox("Select a review to generate an auto-response:", review_options)

        if st.button("Generate Auto-Response"):
            review_index = review_options.index(selected_review)   #identify which review is selected and generate the appropriate response
            review_data = selected_columns.iloc[review_index]
            response = generate_auto_response(review_data["Sentiment Label"], review_data["Text"])

            recipient_email = ""   #email response to customer (actual email id will replace blank)
            subject = "Response to Your Review"
            body = f"Dear Customer,\n\n{response}\n\nBest regards,\nBT Feedback Team"

            mailto_link = f"mailto:{recipient_email}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}" #link to email 
            st.markdown(f"[Create Email Draft]({mailto_link})", unsafe_allow_html=True)

    except FileNotFoundError:
        st.error("The cleaned reviews file was not found. Please upload data first.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
