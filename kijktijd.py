# -*- coding: utf-8 -*-
# @Author: Tom Lotze
# @Date:   2020-03-25 11:22
# @Last Modified by:   Tom Lotze
# @Last Modified time: 2020-03-25 15:51


# Moet maandag avond gerund wordens

import tweepy
import requests
from bs4 import BeautifulSoup as BS
import locale
from datetime import date

from simple_tweet import *


def kijktijd(url="https://kijkonderzoek.nl/kijkcijfers/tv-kijkcijfers/weekrapporten/weekoverzichten"):

    # retrieve the website
    response = requests.get(url)
    html = BS(response.text, "html.parser")

    # extract text in hyperlinks
    div = html.find("div", class_="el-content uk-panel uk-margin-top")
    weken = list([i.string for i in div.find_all('a', target="_blank")])

    return weken


def extract_from_week(week):
    [kijktijd, schermtijd, marktaandeel] = week.split(" min.,")
    week, kijktijd, schermtijd = int(kijktijd.split()[2][:-1]), int(kijktijd.split()[-1]), int(schermtijd.split()[-1])

    return week, kijktijd, schermtijd

def tweet(last_week, previous_week):
    _, kijktijd_prev, schermtijd_prev = extract_from_week(previous_week)
    week, kijktijd_curr, schermtijd_curr = extract_from_week(last_week)

    delta_kijktijd = (kijktijd_curr - kijktijd_prev)
    kijktijd_percentage = int(delta_kijktijd / kijktijd_prev * 100)
    delta_schermtijd = (schermtijd_curr - schermtijd_prev)
    schermtijd_percentage = int(delta_schermtijd / schermtijd_prev * 100)

    if delta_kijktijd >= 0:
        msg = f"In week {week} was de gemiddelde kijktijd per dag {kijktijd_curr} min. Dit is een toename van {delta_kijktijd} min. (+{kijktijd_percentage}%) t.o.v. vorige week.\n"
    else:
        msg = f"In week {week} was de gemiddelde kijktijd per dag {kijktijd_curr} min. Dit is een afname van {delta_kijktijd} min. t.o.v. vorige week (-{kijktijd_percentage}%).\n"

    if delta_schermtijd >= 0:
        msg += f"Verder is de schermtijd met {schermtijd_percentage}% ({delta_schermtijd} min.) toegenomen tot gemiddeld {schermtijd_curr} minuten per dag t.o.v. vorige week."
    else:
        msg+= f"Verder is de schermtijd met {-schermtijd_percentage}% ({delta_schermtijd} min.) afgenomen t.o.v. vorige week, tot gemiddeld {schermtijd_curr} minuten per dag."

    send_tweet(msg)



if __name__ == "__main__":
    curr_week_nr = date.today().isocalendar()[1]
    weken = kijktijd()

    last_week = str(weken[0])
    previous_week = str(weken[2])

    tweet(last_week, previous_week)
