# -*- coding: utf-8 -*-
# python 3
# @Author: Tom Lotze
# @Date:   2020-02-18 18:49:26
# @Last Modified by:   Tom Lotze
# @Last Modified time: 2020-02-18 19:05:37

import tweepy
import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime, timedelta, date
from scrape_kijkcijfers import *
from simple_tweet import *

top = get_top()

yesterday = (date.today() - timedelta(days=1))

msg = f"De kijkcijfers voor {yesterday.strftime('%d %b %Y')}:\n\n"

for i in range(5):
    msg += f"{i+1}: {top[i][0]} met {top[i][1]} kijkers\n"


send_tweet(msg)

