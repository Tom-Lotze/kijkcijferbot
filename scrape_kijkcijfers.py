# -*- coding: utf-8 -*-
# python 3
# @Author: Tom Lotze
# @Date:   2020-02-18 18:08:55
# @Last Modified by:   Tom Lotze
# @Last Modified time: 2020-02-18 20:55:10

import requests
from bs4 import BeautifulSoup as BS


def get_top(url="https://kijkonderzoek.nl/"):

    # retrieve the website 
    response = requests.get(url)
    html = BS(response.text, "html.parser")
    # print(html.prettify())

    # extract titles and viewing numbers
    titles = html.find_all("td", class_="kc_cdtitle", limit=25)
    viewings = html.find_all("td", class_="kc_cdrt0", limit=25)

    # construct a ranking
    ranking = [(title.div.string, number.string) for title, number in zip(titles, viewings)]
    
    return ranking


