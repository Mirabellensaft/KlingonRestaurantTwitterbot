#!/usr/bin/env python

import sys
import time
import tweepy


from twit_conf import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status("some awesome tweet")
#time.sleep(24*60*60)
