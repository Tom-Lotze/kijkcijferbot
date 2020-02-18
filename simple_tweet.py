# -*- coding: utf-8 -*-
# python 3
# @Author: Tom Lotze
# @Date:   2020-02-18 17:55:02
# @Last Modified by:   Tom Lotze
# @Last Modified time: 2020-02-18 18:57:58



# importing tweepy module 
import tweepy 
  
# personal details 
consumer_key ="kt2IB6p4Q04CLoxKRA3Ypjxx1"
consumer_secret ="uDktAWA4MNkdLBxFzsxiY4fide8lQRG1FExPqFOehA34JTPXwG"
access_token ="1229809093730275335-pIYQQgyavikJedzdTdH4UUQXQ4CoCk"
access_token_secret ="JJm0IhrciAepUE6rzF4WMmdBOoqDTxvZOkA2ZBM5yxlax"
  

def send_tweet(msg):
    # authentication of consumer key and secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
      
    # authentication of access token and secret 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth) 
      
    # update the status 
    api.update_status(status=msg) 