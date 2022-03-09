import tweepy
import os
import pymongo
import logging


##################
# Authentication #
##################
BEARER_TOKEN = "''''"


#Mongo db 
mongodb_client = pymongo.MongoClient("mongodb://mongodb:27017/")
db = mongodb_client.twitter

#tweepy client
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    wait_on_rate_limit=True,
)

#####################
# Search for Tweets #
#####################


# - Tweets About Berlin:
search_query = "berlin -is:retweet -is:reply -is:quote lang:en -has:links"

cursor = tweepy.Paginator(
    method=client.search_recent_tweets,
    query=search_query,
    tweet_fields=['author_id', 'created_at', 'public_metrics']
).flatten(limit=20)

  

for tweet in cursor:    
    db.tweets.insert_one(dict(tweet))
    print(tweet.text+'\n')
#collection = db.tweets