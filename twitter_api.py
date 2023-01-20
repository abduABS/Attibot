"""
The main python file for the Attibot Twitter bot.
Code has been used in conjecture with code provided from GitHub Copilot, DataCamp, and ChatGPT.

Written by: Abdu Sallouh Twitter: @abdusallouh GitHub: @abduABS
"""
import tweepy
import configparser
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from os import environ

# # Read config file
# config = configparser.ConfigParser(interpolation=None)
# config.read('config.ini')
#
# # Import API keys
# api_key = config['twitter']['api_key']
# api_key_secret = config['twitter']['api_key_secret']
#
# # Import bearer token
# bearer_token = config['twitter']['bearer_token']
#
# # Import access token
# access_token = config['attibot']['token']
# access_token_secret = config['attibot']['secret']
#
# # Import client tokens
# client_ID = config['twitter']['client_ID']
# client_Id_secret = config['twitter']['client_Id_secret']


# Import API keys
api_key = environ['api_key']
api_key_secret = environ['api_key_secret']

# Import bearer token
bearer_token = environ['bearer_token']

# Import access token
access_token = environ['token']
access_token_secret = environ['secret']

# Import client tokens
client_ID = environ['client_ID']
client_Id_secret = environ['client_Id_secret']

# Authentication
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Account to track
track_account = "TheAttiBot"

# Get the most recent tweet that mentions the track account
saved_id = ''
while True:
    mentions = api.search_tweets(q=f"@{track_account}", count=1)

    # Extract the text of the tweet
    most_recent_mention = mentions[0].text
    keyword = most_recent_mention.split()[-1].lower()

    # Extract the user screen name
    screen_name = mentions[0].user.screen_name

    # Extract the tweet id
    tweet_id = mentions[0].id

    if tweet_id != saved_id:
        saved_id = tweet_id
        # Print the most recent mention
        print(most_recent_mention)

        # Tweepy client
        client = tweepy.Client(bearer_token=bearer_token)
        response = client.search_recent_tweets(keyword, max_results=20)

        # Get the tweets
        tweets = response[0]

        # Initialize the VADER sentiment analyzer
        analyzer = SentimentIntensityAnalyzer()

        # Initialize the sentiment score
        sentiment = 0

        # The tweets to be analyzed
        for i in range(len(tweets)):
            # Get the text of the tweet
            text = tweets[i]['text']

            # Get the sentiment scores
            sentiment_scores = analyzer.polarity_scores(text)

            # Print the sentiment score
            # print(sentiment_scores)

            # Get the compound score
            compound_score = sentiment_scores['compound']

            # Print the compound score
            # print(compound_score)

            # Sum up the compound scores
            sentiment += compound_score

        # Overall aggregated sentiment
        sentiment = sentiment / len(tweets)
        rating = 'Positive' if sentiment > 0 else 'Negative'

        # The reply message
        reply_message = f'I have looked up "{keyword}" on twitter. The average sentiment is {rating} with a score of {sentiment:.2f}.'
        print(reply_message)


        # Reply to the tweet
        api.update_status(
            f"@{screen_name} {reply_message}",
            in_reply_to_status_id=tweet_id
        )

        # Log for debugging
        print("Reply sent!")

        time.sleep(120)









