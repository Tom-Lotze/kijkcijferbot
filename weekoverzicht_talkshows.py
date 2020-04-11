# -*- coding: utf-8 -*-
# @Author: Tom Lotze
# @Date:   2020-04-10 17:13
# @Last Modified by:   Tom Lotze
# @Last Modified time: 2020-04-11 15:27

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

    for single_data in (today - timedelta(n) for n in range(5, 0, -1)):
        formatted_date = single_data.strftime('%d %B %Y')
        filename = formatted_date + ".json"

        with open("data/"+filename) as f:
            ranking = json.load(f)


            if ranking:
                days.append(formatted_date)
                kijkcijfers_jinek = find_kijkcijfers_json(ranking, "JINEK")
                kijkcijfers_op1 = find_kijkcijfers_json(ranking, "OP1")
                jinek.append(kijkcijfers_jinek)
                op1.append(kijkcijfers_op1)

    return days, jinek, op1


def find_rank_json(ranking, name):
    for k, v in ranking.items():
        if v["name"] == name:
            return int(k)

    return 0

def find_kijkcijfers_json(ranking, name):
    for k, v in ranking.items():
        if v["name"] == name:
            return int(v['kijkers'].replace(".", "")) / 1000

    return 0



def graph_jinek_op1(days, jinek, op1):

    week_nr = date.today().isocalendar()[1]

    image_path = f"./talkshow_graphs/{week_nr}.png"

    plt.figure()

    plt.grid()
    plt.title(f"Kijkcijfers in de #talkshowoorlog in week {week_nr}")

    plt.scatter(days, jinek, label="Jinek", marker="o", color="blue", s=40)
    plt.scatter(days, op1, label="Op1", marker="x", color="red", s=40)

    plt.xlabel("Datum")
    plt.ylabel("Kijkcijfers x 1000")

    plt.legend()


    plt.savefig(image_path)


    return image_path








if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, locale="nl_NL")
    os.makedirs("data", exist_ok=True)
    os.makedirs("talkshow_graphs", exist_ok=True)


    days, jinek_kijkcijfers, op1_kijkcijfers = get_data_talkshows()

    image_path = graph_jinek_op1(days, jinek_kijkcijfers, op1_kijkcijfers)

    status = "Hier het overzicht van de talkshowoorlog van afgelopen week! #talkshowoorlog #Op1 #Jinek"

    send_media_tweet(image_path, status)
