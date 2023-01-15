import tweepy
import configparser

#read configs
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
bearer_token = config['twitter']['bearer_token']

access_token = config['attibot']['token']
access_token_secret = config['attibot']['secret']

client_ID = config['twitter']['client_ID']
client_Id_secret = config['twitter']['client_Id_secret']

print(api_key)

#authentication
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#tweepy client
client = tweepy.Client(bearer_token=bearer_token,return_type=list)
tweets = client.search_recent_tweets('potato')
for tweet in tweets:
    print(tweet)



# # Account to track
# track_account = "TheAttiBot"
#
# # Get the most recent tweet that mentions the track account
# mentions = api.search_tweets(q=f"@{track_account}", count=1)
#
# # Extract the text of the tweet
# most_recent_mention = mentions[0].text
#
# # Extract the user screen name
# screen_name = mentions[0].user.screen_name
#
# # Extract the tweet id
# tweet_id = mentions[0].id
#
# # Print the most recent mention
# print(most_recent_mention)
#
# # Your reply message
# reply_message = "I have noticed you. This is an automated message"
#
# # Reply to the tweet
# api.update_status(
#     f"@{screen_name} {reply_message}",
#     in_reply_to_status_id=tweet_id
# )
#
# print("Reply sent!")









