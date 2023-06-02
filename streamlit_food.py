import streamlit as st
from configs.config import csv_of_food_delivery_apps, csv_of_top_restaurants_usernames_in_hyderabad,\
    csv_of_top_restaurants_usernames_in_bangalore, csv_of_merged_food, food_delivery_apps,\
    top_restaurants_usernames_in_hyderabad,top_restaurants_usernames_in_bangalore
from mat_plot import twitter_plot, sentiment_plot, get_plot_info_by_user


st.image('logo.png', width=150)

# dropdowns
date_select = st.sidebar.selectbox('Date: ', ['2023', '2022', '2021', '2020'])
info_select = st.sidebar.selectbox('Y axis:', ['number of tweets', 'number of likes', 'number of retweets'])
usertype_select = st.sidebar.selectbox('Select user type(X-axis):', ['All', 'food delivery apps', 'top restaurants in hyderabad', 'top restaurants in bangalore'])
username_select = None
if usertype_select == 'food delivery apps':
    username_select = st.sidebar.selectbox('Select user name(New X-axis):', ['All', 'zomato', 'Swiggy', 'DunzoIt', 'faasos', 'letsblinkit'])
if usertype_select == 'top restaurants in hyderabad':
    username_select = st.sidebar.selectbox('Select user name(New X-axis):', ['All', 'cafebaharhyd', 'pistahousehyd', 'CafeCoffeeDay', 'MehfilBiryani', 'Almondsforyou' , 'Creamstone'])
if usertype_select == 'top restaurants in bangalore':
    username_select = st.sidebar.selectbox('Select user name(New X-axis):', ['All', 'FarziCafe', 'KFC_India', 'PizzaHutIN', 'dominos_india', 'absolutebbq', 'CoffeeBrewery'])

# code for info_select, usertype_select & username_select
if st.sidebar.button('View chart'):
    if usertype_select == "All":
        if info_select == "number of tweets":
            twitter_plot(csv_of_merged_food, 'total_tweets')
        elif info_select == "number of likes":
            twitter_plot(csv_of_merged_food, 'total_likes')
        elif info_select == 'number of retweets':
            twitter_plot(csv_of_merged_food, 'total_retweets')
        st.image('food.jpg')

    elif usertype_select == "food delivery apps":
        if username_select == 'All':
            if info_select == "number of tweets":
                twitter_plot(csv_of_food_delivery_apps, 'total_tweets')
            elif info_select == "number of likes":
                twitter_plot(csv_of_food_delivery_apps, 'total_likes')
            elif info_select == 'number of retweets':
                twitter_plot(csv_of_food_delivery_apps, 'total_retweets')
            st.image('food.jpg')
        elif username_select == 'zomato':
            if info_select == "number of tweets":
                get_plot_info_by_user(csv_of_food_delivery_apps, 'zomato', 'total_tweets')
            elif info_select == "number of likes":
                get_plot_info_by_user(csv_of_food_delivery_apps, 'zomato', 'total_likes')
            elif info_select == 'number of retweets':
                get_plot_info_by_user(csv_of_food_delivery_apps, 'zomato', 'total_retweets')
            st.image('user_food.jpg')
        elif username_select == 'Swiggy':
            if info_select == "number of tweets":
                get_plot_info_by_user(csv_of_food_delivery_apps, 'Swiggy', 'total_tweets')
            elif info_select == "number of likes":
                get_plot_info_by_user(csv_of_food_delivery_apps, 'Swiggy', 'total_likes')
            elif info_select == 'number of retweets':
                get_plot_info_by_user(csv_of_food_delivery_apps, 'Swiggy', 'total_retweets')
            st.image('user_food.jpg')
        elif username_select == 'DunzoIt':
            if info_select == "number of tweets":
                get_plot_info_by_user(csv_of_food_delivery_apps, 'DunzoIt', 'total_tweets')
            elif info_select == "number of likes":
                get_plot_info_by_user(csv_of_food_delivery_apps, 'DunzoIt', 'total_likes')
            elif info_select == 'number of retweets':
                get_plot_info_by_user(csv_of_food_delivery_apps, 'DunzoIt', 'total_retweets')
            st.image('user_food.jpg')
        elif username_select == 'faasos':
            if info_select == "number of tweets":
                get_plot_info_by_user(csv_of_food_delivery_apps, 'faasos', 'total_tweets')
            elif info_select == "number of likes":
                get_plot_info_by_user(csv_of_food_delivery_apps, 'faasos', 'total_likes')
            elif info_select == 'number of retweets':
                get_plot_info_by_user(csv_of_food_delivery_apps, 'faasos', 'total_retweets')
            st.image('user_food.jpg')
        elif username_select == 'letsblinkit':
            if info_select == "number of tweets":
                get_plot_info_by_user(csv_of_food_delivery_apps, 'letsblinkit', 'total_tweets')
            elif info_select == "number of likes":
                get_plot_info_by_user(csv_of_food_delivery_apps, 'letsblinkit', 'total_likes')
            elif info_select == 'number of retweets':
                get_plot_info_by_user(csv_of_food_delivery_apps, 'letsblinkit', 'total_retweets')
            st.image('user_food.jpg')

    elif usertype_select == "top restaurants in hyderabad":
        if info_select == "number of tweets":
            twitter_plot(csv_of_top_restaurants_usernames_in_hyderabad, 'total_tweets')
        elif info_select == "number of likes":
            twitter_plot(csv_of_top_restaurants_usernames_in_hyderabad, 'total_likes')
        elif info_select == 'number of retweets':
            twitter_plot(csv_of_top_restaurants_usernames_in_hyderabad, 'total_retweets')
        st.image('food.jpg')

    elif usertype_select == "top restaurants in bangalore":
        if info_select == "number of tweets":
            twitter_plot(csv_of_top_restaurants_usernames_in_bangalore, 'total_tweets')
        elif info_select == "number of likes":
            twitter_plot(csv_of_top_restaurants_usernames_in_bangalore, 'total_likes')
        elif info_select == 'number of retweets':
            twitter_plot(csv_of_top_restaurants_usernames_in_bangalore, 'total_retweets')
        st.image('food.jpg')


# code for sentiment_user_select
sentiment_user_select = st.sidebar.selectbox('Select user to get average sentiment: ', ['zomato', 'Swiggy', 'DunzoIt', 'faasos', 'letsblinkit'])
if st.sidebar.button('View sentiment'):
    if sentiment_user_select == 'zomato':
        sentiment_plot('zomato')
    elif sentiment_user_select == 'Swiggy':
        sentiment_plot('Swiggy')
    elif sentiment_user_select == 'DunzoIt':
        sentiment_plot('DunzoIt')
    elif sentiment_user_select == 'faasos':
        sentiment_plot('faasos')
    elif sentiment_user_select == 'letsblinkit':
        sentiment_plot('letsblinkit')

    st.image('sentiment.jpg')
