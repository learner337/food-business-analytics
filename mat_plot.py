import pandas as pd
import matplotlib.pyplot as plt
# from configs.config import csv_of_food_delivery_apps
from sentiment_analysis import get_sentiment_score_by_user


def twitter_plot(csv_file, y_axis):
    df = pd.read_csv(csv_file)

    user_wise_total_num_of_info = dict()
    for index in range(df.shape[0]):
        name = df.loc[index]['name']
        likes_of_a_tweet = df.loc[index]['likes']
        retweets_of_a_tweet = df.loc[index]['retweets']
        if name not in user_wise_total_num_of_info:
            if y_axis == "total_tweets" :
                user_wise_total_num_of_info[name] = 1
            elif y_axis == "total_likes":
                user_wise_total_num_of_info[name] = likes_of_a_tweet
            elif y_axis == "total_retweets":
                user_wise_total_num_of_info[name] = retweets_of_a_tweet
        else:
            if y_axis == "total_tweets":
                user_wise_total_num_of_info[name] = user_wise_total_num_of_info[name] + 1
            elif y_axis == "total_likes":
                user_wise_total_num_of_info[name] = user_wise_total_num_of_info[name] + likes_of_a_tweet
            elif y_axis == "total_retweets":
                user_wise_total_num_of_info[name] = user_wise_total_num_of_info[name] + retweets_of_a_tweet

    plt.figure(figsize=(20, 10))
    plt.bar(x=user_wise_total_num_of_info.keys(), height=user_wise_total_num_of_info.values())
    plt.savefig('food.jpg')


def get_plot_info_by_user(csv, username, y_axis):
    df = pd.read_csv(csv)
    single_user_info_list = []

    for index in range(len(df['name'])):
            if y_axis == 'total_tweets':
                if df['name'].loc[index] == username:
                    single_user_info_list.append(1)
            elif y_axis == 'likes':
                if df['name'].loc[index] == username:
                    likes_of_a_tweet = df['likes'].loc[index]
                    single_user_info_list.append(likes_of_a_tweet)
            elif y_axis == 'retweets':
                if df['name'].loc[index] == username:
                    retweets_of_a_tweet = df['likes'].loc[index]
                    single_user_info_list.append(retweets_of_a_tweet)

    total_info = sum(single_user_info_list)

    plt.figure(figsize=(20, 10))
    plt.bar(x=username, height=total_info)
    plt.savefig('user_food.jpg')


def sentiment_plot(user):
    average = get_sentiment_score_by_user(user)
    plt.bar(x=user, height=average)
    plt.savefig('sentiment.jpg')
