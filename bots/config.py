# twitterBot/bots/congig.py

import tweepy
import logging
import os

logger = logging.getLogger()

def createApi():
    consumerKey = os.getenv("CONSUMER_KEY")
    consumerSecret = os.getenv("CONSUMER_SECRET")
    accessToken = os.getenv("ACCESS_TOKEN")
    accessTokenSecret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    
    api = tweepy.API(auth, wait_on_rate_limit = True,
        wait_on_rate_limit_notify = True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info = True)
        raise e
    
    logger.info("API created")
    return api