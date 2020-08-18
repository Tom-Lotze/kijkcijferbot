import requests
from bs4 import BeautifulSoup as BS


def get_top(url="https://kijkonderzoek.nl/"):

    # retrieve the website
    response = requests.get(url)
    html = BS(response.text, "html.parser")

    # extract titles and viewing numbers
    titles = html.find_all("td", class_="kc_cdtitle", limit=25)
    viewings = html.find_all("td", class_="kc_cdrt0", limit=50)

    avg_viewings = [viewings[i] for i in range(0,50,2)]
    
    # construct a ranking
    ranking = [(title.div.string, number.string) for title, number in zip(titles, avg_viewings)]
    
    return ranking

print(get_top())
