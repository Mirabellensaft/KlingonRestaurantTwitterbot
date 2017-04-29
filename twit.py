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

while True:
    curse = random.choice(curses)
    print curse
    #api.update_status(curse)
    time.sleep(random.randint(12*60*60, 24*60*60))
