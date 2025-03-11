import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load customer reviews data
reviews = pd.read_csv("data/customer_reviews.csv")

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Generate sentiment scores
reviews["sentiment_score"] = reviews["review_text"].apply(lambda x: analyzer.polarity_scores(str(x))["compound"])

# Normalize sentiment to 0-1 scale
reviews["sentiment_score"] = (reviews["sentiment_score"] + 1) / 2

# Save updated data
reviews.to_csv("data/customer_reviews_with_sentiment.csv", index=False)

print("✅ Sentiment scores generated and saved.")
