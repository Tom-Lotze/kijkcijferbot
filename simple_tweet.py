# importing tweepy module 
import tweepy 
from get_keys import *
  
# personal details 
consumer_key, consumer_secret, access_token, access_token_secret = get_personal_keys()
  

def send_tweet(msg):
    # authentication of consumer key and secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
      
    # authentication of access token and secret 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth) 
      
    # update the status 
    api.update_status(status=msg) 