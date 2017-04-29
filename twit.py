#!/usr/bin/env python

import sys
import time
import tweepy
import random


from twit_conf import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Tweets random curses in time intervals between 12 and 24h
f = open('curses.txt')
curses = f.readlines()
curses = [c.strip() for c in curses]

#while True:
    #curse = random.choice(curses)
    #print curse
    #api.update_status(curse)
    #time.sleep(random.randint(12*60*60, 24*60*60))

# answers mentions with random curses
id_list_old = []
f_id = open('id_list_old.txt')
old_mentions = f_id.readlines()
f_id.close()
id_list_old = [int(id_str) for id_str in old_mentions]

while True:
    mentions = api.mentions_timeline()
    for mention in mentions:
        if mention.id not in id_list_old:
            curse = random.choice(curses)
            print ('@%s %s' % (mention.user.screen_name, curse), mention.id)
            api.update_status('@%s %s!' % (mention.user.screen_name, curse), mention.id)
            id_list_old.append(mention.id)
            f_id = open('id_list_old.txt', 'a')
            f_id.write("%s\n" % mention.id)
            f_id.close()
    time.sleep(60)
