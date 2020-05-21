import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("ZJiRhsMaKX9V1x0jAifoJwoht", 
    "BXeGiup15ApHZZy780OoErsAc3KU5km6j6YbLmijqpyoZAMUjL")

# Acess token & access token secret(only able to see one time); last generated: May 20, 3:22
auth.set_access_token("963270419401859072-J050kT7pVfEyzj7fAPbYUDFwC1F17Ep",
    "m26YTzVqfrd5ZqvE6UFHK6kYLrzMDNHt4EyZsT0Rly8Sy")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("authentication OK")
except:
    print("Error during authentication")