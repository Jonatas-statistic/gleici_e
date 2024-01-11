import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def calc_sentiment_score(text:str):
    sia = SentimentIntensityAnalyzer()
    sentimet_score = sia.polarity_scores(text)
    return sentimet_score


def is_good(text: str):
    sentiment_score = calc_sentiment_score(text)
    if sentiment_score['compound'] > 0:
        return True
    return False
