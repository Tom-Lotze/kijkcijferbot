# -*- coding: utf-8 -*-
# @Author: Tom Lotze
# @Date:   2020-04-10 17:13
# @Last Modified by:   Tom Lotze
# @Last Modified time: 2020-04-11 14:45

import tweepy
from datetime import datetime, timedelta, date
import locale
import os
import json
import time
import matplotlib.pyplot as plt


from simple_tweet import *


"""
This script needs to run on saturday and will tweet a graph
"""


def get_data_talkshows():

    # today will be a saturday
    today = date.today()

    days = []
    jinek = []
    op1 = []

    for single_data in (today - timedelta(n) for n in range(6, 1, -1)):
        formatted_date = single_data.strftime('%d %B %Y')
        filename = formatted_date + ".json"

        with open("data/"+filename) as f:
            ranking = json.load(f)[formatted_date]
            print(formatted_date)
            print(ranking)

            if ranking:
                days.append(formatted_date)
                ranking_jinek = [pair[0] for pair in ranking].index('JINEK')
                ranking_op1 = [pair[0] for pair in ranking].index('OP1')
                jinek.append(ranking_jinek)
                op1.append(ranking_op1)




    breakpoint()






    return days, jinek, op1



def graph_jinkek_op1(days, jinek, op1):

    plt.figure()















if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, locale="nl_NL")
    os.makedirs("data", exist_ok=True)
    os.makedirs("talkshow_graphs", exist_ok=True)


    days, jinek_kijkcijfers, op1_kijkcijfers = get_data_talkshows()

    graph_jinkek_op1(days, jinek_kijkcijfers, op1_kijkcijfers)



    send_media_tweet(imagePath, status)
