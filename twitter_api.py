import tweepy
import configparser
import pandas as pd
import pickle


# Read configs
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
bearer_token = config['twitter']['bearer_token']

access_token = config['attibot']['token']
access_token_secret = config['attibot']['secret']

client_ID = config['twitter']['client_ID']
client_Id_secret = config['twitter']['client_Id_secret']

# Read the model
with open('api_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Authentication
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Account to track
track_account = "TheAttiBot"

# Get the most recent tweet that mentions the track account
mentions = api.search_tweets(q=f"@{track_account}", count=1)

# Extract the text of the tweet
most_recent_mention = mentions[0].text
keyword = most_recent_mention.split()[-1].lower()


# Extract the user screen name
screen_name = mentions[0].user.screen_name

# Extract the tweet id
tweet_id = mentions[0].id

# Print the most recent mention
print(most_recent_mention)

# Tweepy client
client = tweepy.Client(bearer_token=bearer_token)
response = client.search_recent_tweets(keyword)

tweets = response[0]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(tweets)
df = df.drop(columns=["edit_history_tweet_ids", "id"])
print(df)

# Predict the sentiment
print(model.predict(df))

# for tweet in response[0]:
#     print(tweet)


# Your reply message
# reply_message = f'I have looked up {most_recent_mention} on twitter. Nothing yet to report.'
#
# # Reply to the tweet
# api.update_status(
#     f"@{screen_name} {reply_message}",
#     in_reply_to_status_id=tweet_id
# )
#
# print("Reply sent!")









