from api.scraping_tweets_using_api import get_merged_tweets_of_multiple_users_using_api, get_tweets_using_keywords
from configs.config import food_delivery_apps, csv_of_food_delivery_apps, csv_of_tweets_using_keywords, top_restaurants_usernames_in_hyderabad,\
    top_restaurants_usernames_in_bangalore, csv_of_top_restaurants_usernames_in_hyderabad, csv_of_top_restaurants_usernames_in_bangalore, \
    csv_of_food_delivery_apps_latest, csv_of_top_restaurants_usernames_in_bangalore_latest, csv_of_top_restaurants_usernames_in_hyderabad_latest
from utils.utils import date_separator
import csv


def create_csv():
    tweets_of_multiple_users = get_merged_tweets_of_multiple_users_using_api(food_delivery_apps)                     # function called
    # tweets_of_keywords = get_tweets_using_keywords()               for keywords function                                                    # function called
    with open(csv_of_food_delivery_apps_latest, 'w', newline='', encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Name','Screen name','Tweet id','Tweet text','Date','Time','Retweets','Replied to','Likes', "Hashtags"])
        for tweet in tweets_of_multiple_users:
            # for i in tweet:                                       for keywords function
                date, time = date_separator(tweet.created_at)  # function called
                hashtags_list = []
                hashtags = tweet.entities["hashtags"]
                for hashtag in hashtags:
                    hashtag_text = hashtag["text"]
                    hashtags_list.append(hashtag_text)
                hashtags_joined = ','.join(hashtags_list)
                csv_writer.writerow([tweet.user.name,
                                     tweet.user.screen_name,
                                     tweet.id,
                                     tweet.text,
                                     date,
                                     time,
                                     tweet.retweet_count,
                                     tweet.in_reply_to_screen_name,
                                     tweet.favorite_count,
                                     hashtags_joined])


create_csv()

