import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")  
sia = SentimentIntensityAnalyzer()

def analyze_sentiment():
    df = pd.read_csv("data/cleaned_reviews.csv")
    df["Sentiment"] = df["Text"].apply(lambda x: sia.polarity_scores(x)["compound"])
    def categorize_sentiment(score):
        if score <= -0.5:
            return "Very Negative"
        elif -0.5 < score <= 0:
            return "Negative"
        elif 0 < score <= 0.5:
            return "Neutral"
        else:
            return "Positive"

    # Add labels to the DataFrame
    df["Sentiment Label"] = df["Sentiment"].apply(categorize_sentiment)
    return df

