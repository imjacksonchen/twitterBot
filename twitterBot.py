import tweepy
import json

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def onStatus(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def onError(self, status):
        print("Error detected")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("ZJiRhsMaKX9V1x0jAifoJwoht", 
    "BXeGiup15ApHZZy780OoErsAc3KU5km6j6YbLmijqpyoZAMUjL")

# Acess token & access token secret(only able to see one time); last generated: May 20, 3:22
auth.set_access_token("963270419401859072-J050kT7pVfEyzj7fAPbYUDFwC1F17Ep",
    "m26YTzVqfrd5ZqvE6UFHK6kYLrzMDNHt4EyZsT0Rly8Sy")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# Streaming
tweetsListener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweetsListener)
stream.filter(track = ["Python", "Django", "Tweepy"], languages = ["en"])

# try:
#     api.verify_credentials()
#     print("authentication OK")
# except:
#     print("Error during authentication")

# User timeline
# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")

# Tweets
# api.update_status("Missing the music from the 2012")

# Users
# user = api.get_user("KingJames")

# print("User details:")
# print(user.name)
# print(user.description)
# print(user.location)

# print("Last 20 Followers:")
# for follower in user.followers():
#     print(follower.name)

# Followers
# api.create_friendship("realpython")

# api.destroy_friendship("realpython")

# User followers
# followers = api.friends()
# for follower in followers:
#     print(follower.name)

# Account description
# api.update_profile(description = "I like food")

# Likes; example likes the first tweet on the user's home timeline
# tweets = api.home_timeline(count = 1)
# tweet = tweets[0]
# print(f"Liking tweet {tweet.id} of {tweet.author.name}")
# api.create_favorite(tweet.id)

# Blocking users; example prints out the people block for the user
# for block in api.blocks():
#     print(block.name)

# Search
# for tweet in api.search(q = "Python", lang = "en", rpp = 10):
#     print(f"{tweet.user.name}:{tweet.text}")

# Trends
# trends_result = api.trends_place(23424977)
# for trend in trends_result[0]["trends"]:
#     print(trend["name"])

# listOfLocationTrends = api.trends_available()
# for trendLocation in listOfLocationTrends:
#     name = trendLocation["name"]
#     id = trendLocation["woeid"]
#     print(f"{name}:{id}")