# -*- coding: utf-8 -*-
# python 3
# @Author: Tom Lotze
# @Date:   2020-02-18 17:55:02
# @Last Modified by:   Tom Lotze
# @Last Modified time: 2020-02-18 19:20:22



# importing tweepy module 
import tweepy 
from get_keys import *
  
# personal details 
consumer_key, consumer_secret, access_token, access_token_secret = get_personal_keys()
  
# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
  
# update the status 
api.update_status(status ="Test: Hello Everyone !") 
