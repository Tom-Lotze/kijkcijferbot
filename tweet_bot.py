import tweepy
import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime, timedelta, date
import locale
from scrape_kijkcijfers import *
from simple_tweet import *

# set locale settings
locale.setlocale(locale.LC_ALL, locale="nl_NL")

###### KIJKCIJFERS

k = 5
ranking = get_top()
yesterday = (date.today() - timedelta(days=1))

msg1 = f"De kijkcijfers voor {yesterday.strftime('%d %B %Y')}:\n\n"

for i in range(k):
    if len(ranking[i][0])>12:
        msg1 += f"{i+1}: {ranking[i][0]}: {ranking[i][1]}\n"
    else:
         msg1 += f"{i+1}: {ranking[i][0]}: {ranking[i][1]}\n"

# send tweet with kijkcijfers
print(msg1)
#send_tweet(msg1)







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

    #send_tweet(msg2)




