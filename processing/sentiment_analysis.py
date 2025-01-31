import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(asin=None):
    df = pd.read_csv("data/review_file.csv")

    df["Sentiment"] = df["Text"].apply(lambda x: sia.polarity_scores(str(x))["compound"])


    df["Sentiment Label"] = df["Sentiment"].apply(
        lambda score: (
            "Very Negative" if score <= -0.5 else
            "Negative" if score <= 0 else
            "Neutral" if score <= 0.5 else
            "Positive"
        )
    )

    return df
