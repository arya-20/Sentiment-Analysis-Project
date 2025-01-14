import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")  
sia = SentimentIntensityAnalyzer()

def analyze_sentiment():
    df = pd.read_csv("data/cleaned_reviews.csv")
    df["Sentiment"] = df["Text"].apply(lambda x: sia.polarity_scores(x)["compound"])
    return df

