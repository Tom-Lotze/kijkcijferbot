import tweepy

from get_keys import *

# personal details
consumer_key, consumer_secret, access_token, access_token_secret = get_personal_keys()

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


tweets = api.mentions_timeline()
for tweet in tweets:
    try:
        tweet.favorite()
    except:
        pass
    try:
        tweet.user.follow()
    except:
        pass
