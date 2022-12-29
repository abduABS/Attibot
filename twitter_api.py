import tweepy
import configparser

#read configs
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
bearer_token = config['twitter']['bearer_token']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

client_ID = config['twitter']['client_ID']
client_Id_secret = config['twitter']['client_Id_secret']

print(api_key)

#authentication
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()

print(public_tweets)