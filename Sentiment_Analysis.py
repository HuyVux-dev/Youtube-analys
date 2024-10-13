import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the vader_lexicon data
# nltk.download("vader_lexicon")
# Create a sentiment analyzer
analyzer = SentimentIntensityAnalyzer()
# Analyze some text
text = "In this blog post, we showed you how to use NTLK to perform sentiment analysis in Python."
scores = analyzer.polarity_scores(text)
print(scores)

# Classify the text as positive, neutral, or negative
if scores['compound'] >= 0.5:
    print("Positive")
elif scores['compound'] > -0.5:
    print("Neutral")
else:
    print("Negative")