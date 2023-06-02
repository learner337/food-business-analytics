from textblob import TextBlob
import pandas as pd
from configs.config import csv_of_food_delivery_apps, csv_of_sentiment_analysis
import csv


df = pd.read_csv(csv_of_food_delivery_apps)
list_for_usernames = []
list_for_text = []
list_for_sentiment_score = []
list_for_sentiment_type = []
num_of_rows = 16144


def create_csv_of_sentiment():
    sentiment_type = None
    for i in range(num_of_rows):
        username = df['name'].loc[i]
        tweet_text = df['tweet text'].loc[i]
        tweet_text = str(tweet_text)
        analysis = TextBlob(tweet_text)
        sentiment_score = analysis.sentiment.polarity
        if sentiment_score > 0.3:
            sentiment_type = 'Positive'
        elif 0.3 > sentiment_score > -0.3:
            sentiment_type = 'Neutral'
        elif sentiment_score < -0.3:
            sentiment_type = 'Negative'

        list_for_usernames.append(username)
        list_for_text.append(tweet_text)
        list_for_sentiment_score.append(sentiment_score)
        list_for_sentiment_type.append(sentiment_type)

    with open(csv_of_sentiment_analysis, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Tweet', 'Sentiment score', 'Sentiment type'])
        for i in range(num_of_rows):
            writer.writerow([list_for_usernames[i], list_for_text[i], list_for_sentiment_score[i], list_for_sentiment_type[i]])


# create_csv_of_sentiment()


def get_sentiment_score_by_user(username):
    list_for_sentiment_score_by_user = []
    average = None
    for i in range(num_of_rows):
        if df['name'].loc[i] == username:
            tweet_text = df['tweet text'].loc[i]
            tweet_text = str(tweet_text)
            analysis = TextBlob(tweet_text)
            sentiment_score = analysis.sentiment.polarity
            list_for_sentiment_score_by_user.append(sentiment_score)
            average = sum(list_for_sentiment_score_by_user)/len(list_for_sentiment_score_by_user)
    return average
