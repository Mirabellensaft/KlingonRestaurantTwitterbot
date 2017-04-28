#!/usr/bin/env python

import sys
import time
import tweepy
import random


from twit_conf import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

f = open('curses.txt')
curses = f.readlines()
curse = random.choice(curses)

print curse
api.update_status(curse)
#time.sleep(24*60*60)
