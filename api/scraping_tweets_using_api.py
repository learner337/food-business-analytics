import tweepy
from configs.config import api_key, api_key_secret, access_token_secret, access_token,\
    top_restaurants_names_in_hyderabad, top_restaurants_usernames_in_hyderabad


def get_tweets_of_a_user(username, api):
    # tweets = api.user_timeline(screen_name=username, count=2)
    # return tweets
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=username).items(9):
        yield tweet


def get_merged_tweets_of_multiple_users_using_api(user_names):
    all_tweets = []
    auth = tweepy.OAuth1UserHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    for username in user_names:
        tweets_of_a_user = get_tweets_of_a_user(username, api)                                        # function called
        for tweet in tweets_of_a_user:
            all_tweets.append(tweet)
    return all_tweets


def get_tweets_using_keywords():
    auth = tweepy.OAuth1UserHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    list_of_keywords_tweets = []
    for username in top_restaurants_usernames_in_hyderabad:
        QUERY = '@' + username
        tweets_of_keywords = api.search_tweets(QUERY, lang='en', count=10, tweet_mode='extended', result_type='recent')
        list_of_keywords_tweets.append(tweets_of_keywords)
    return list_of_keywords_tweets


auth = tweepy.OAuth1UserHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# tweets = tweepy.Cursor(api.user_timeline, screen_name="zomato")
tweets = api.search_tweets("zomato", lang='en', count=10, tweet_mode='extended', result_type='recent')
# for tweet in tweets:
print(tweets)
