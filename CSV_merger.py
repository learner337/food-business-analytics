from configs.config import csv_of_top_restaurants_usernames_in_bangalore,csv_of_top_restaurants_usernames_in_hyderabad,\
    csv_of_tweets_using_keywords,csv_of_food_delivery_apps, csv_of_merged_food
import pandas as pd


def csv_to_dataframe():
    merged_dfs_list = []

    df_of_hyd_rests = pd.read_csv(csv_of_top_restaurants_usernames_in_hyderabad)
    df_of_bng_rests = pd.read_csv(csv_of_top_restaurants_usernames_in_bangalore)
    # df_of_keywords = pd.read_csv(csv_of_tweets_using_keywords)
    df_of_del_apps = pd.read_csv(csv_of_food_delivery_apps)

    merged_dfs_list.append(df_of_hyd_rests)
    merged_dfs_list.append(df_of_bng_rests)
    # merged_dfs_list.append(df_of_keywords)
    merged_dfs_list.append(df_of_del_apps)

    merged_dfs = pd.concat(merged_dfs_list)

    merged_dfs.to_csv(csv_of_merged_food)


csv_to_dataframe()


