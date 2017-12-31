#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys
from subjectivity import Sentiment

sentiment = Sentiment()
if len(sys.argv) > 1:
    sentiment.analyze([sys.argv[1]])
else:
    result = sentiment.analyze(['''Distributed denial-of-service attacks, DDoS for short, are a common attack felt by businesses and normal people. When someone preforms a DDoS they are usually trying to deny the person or business traffic or even the ability to use the internet. That's because a DDoS typically tries to flood your network so that everything slows to a crawl and legitimate traffic can't get threw. These attacks are a threat to every business, especially those with a website or any means of taking in information from outside sources. When Blizzard Entertainment launched their newset game Overwatch they became under attack by DDoS bring there launch servers down restricting players from playing the game. This was a major setback for the release for this game, for all the players have to be connected an using a server to play the game. Which was impossible after during the DDoS. While Blizzard never specifically told everyone how they warded off the DDoS attack it can be assumed they used methods such as rate-limiting through routers or switches using Access control list capabilities. The problem with DDoS attacks is that they usually overload you with legitimate content but bad intent. Making it all the more difficult to discern bad traffic from good traffic. Bibliography McDowell, Mindi. (2009, November 4). Understanding denial-of-service attacks. Retrieved April 3, 2017, from https://www.us-cert.gov/ncas/tips/ST04-015'''])
    total = len(result['sentences'])
    n_positive = result['results']['positive']['count']
    n_negative = result['results']['negative']['count']
    n_neutral = result['results']['neutral']['count']
    subjectivity = float(n_positive + n_negative) / total
    objectivity = float(n_neutral) / total
    print subjectivity