import tweepy
import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime, timedelta, date
import locale
import os
import json
import time

from scrape_kijkcijfers import *
from simple_tweet import *

# set locale settings
locale.setlocale(locale.LC_ALL, locale="nl_NL")
os.makedirs("data", exist_ok=True)


def save_json(ranking):
    yesterday = (date.today() - timedelta(days=1)).strftime('%d %B %Y')
    dic = {i: {"name": name, "kijkers": kijkers} for i, (name, kijkers) in enumerate(ranking, start=1)}

    with open(f"./data/{yesterday}.json", "w") as writer:
        json.dump(dic, writer, indent=1)



###### KIJKCIJFERS
k = 5
ranking = get_top()

if not ranking:
    time.sleep(3600)
    ranking = get_top()

if not ranking:
    exit()


# save as json
save_json(ranking)

account_dict = {"JOURNAAL 20 UUR" : "JOURNAAL 20 UUR @NOS",
                "HALF ACHT NIEUWS": "HALF 8 NIEUWS @RTLnieuws",
                "JOURNAAL 18 UUR": "JOURNAAL 18 uur @NOS",
                "CHATEAU MEILAND" : "#chateaumeiland" ,
                "KOPEN ZONDER KIJKEN": "#kopenzonderkijken" }


yesterday = (date.today() - timedelta(days=1))

msg1 = f"De kijkcijfers voor {yesterday.strftime('%d %B %Y')}:\n\n"

for i in range(k):
    try:
        programme = account_dict[ranking[i][0]]
    except:
        programme = ranking[i][0]
        print(programme)
    msg1 += f"{i+1}: {programme}: {ranking[i][1]}\n"

breakpoint()

# send tweet with kijkcijfers
send_tweet(msg1)


###### TALKSHOWTWEET (Talkshows not in the weekend)
if date.today().isoweekday() not in [1, 7]:
    # determine winner of talkshow war
    ranking_jinek = [pair[0] for pair in ranking].index('JINEK')
    ranking_op1 = [pair[0] for pair in ranking].index('OP1')
    jinek_wins = 0
    if ranking_jinek < ranking_op1:
        jinek_wins = 1

    kijkcijfer_jinek = ranking[ranking_jinek][1]
    kijkcijfer_op1 = ranking[ranking_op1][1]

    msg2 = "Ondertussen in de #talkshowoorlog:"

    if jinek_wins:
        msg2 += f"\n@Jinek_RTL werd gisteren beter bekeken dan @op1npo!"
    else:
        msg2 += f"\n@op1npo werd gisteren beter bekeken dan @Jinek_RTL!"

    msg2 += f"\n#Jinek had {kijkcijfer_jinek} kijkers en #Op1 {kijkcijfer_op1}"

    send_tweet(msg2)




