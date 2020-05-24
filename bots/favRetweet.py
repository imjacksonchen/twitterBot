#!/usr/bin/env python
# twittwerBot/bots/favRetweet.py

import tweepy
import logging
from config import createApi
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def onStatus(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I;m its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info = True)
        if not tweet.retweeded:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info = True)
        
    def onError(self, status):
        logger.error(status)

def main(keywords):
    api = createApi()
    tweetsListener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweetsListener)
    stream.filter(track = keywords, languages = ["en"])

if __name__ == "__main__":
    main(["Python", "Tweepy"])