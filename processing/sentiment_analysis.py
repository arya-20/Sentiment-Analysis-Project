import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer() #initialize sentiment intensity analyser

def analyze_sentiment(asin=None):
    df = pd.read_csv("data/review_file.csv")  #load in the reviews from the csv

    df["Sentiment"] = df["Text"].apply(lambda x: sia.polarity_scores(str(x))["compound"]) #apply sentiment analysis using VADER 

    df["Sentiment Label"] = df["Sentiment"].apply(
        lambda score: (
            "Very Negative" if score <= -0.5 else
            "Negative" if score <= 0 else
            "Neutral" if score <= 0.5 else
            "Positive"
        )
    )

    return df
