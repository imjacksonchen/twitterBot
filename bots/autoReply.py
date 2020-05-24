#!/usr/bin/env python
# twitterBot/bots/autoReply.py

import tweepy
import logging
from config import createApi
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def checkMentions(api, keywords, sinceId):
    logger.info("Retriving mentions")
    newSinceId = sinceId
    for tweet in tweepy.Cursor(api.mentions_timeline, sinceId = sinceId).items():
        newSinceId = max(tweet.id, newSinceId)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for key in keywords):
            logeer.info(f"Answering to {tweet.user.name}")

            if not tweet.user.following:
                tweet.user.follow()

            api.update_status(
                status = "Please reach us via DM",
                in_reply_to_status_id = tweet.id,
            )

    return newSinceId

def main():
    api = createApi
    sinceId = 1
    while True:
        sinceId = checkMentions(api, ["help", "support"], sinceId)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()