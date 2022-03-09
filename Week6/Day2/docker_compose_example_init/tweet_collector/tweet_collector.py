import time
from datetime import datetime
import logging
import random
import pymongo
from faker import Faker

# Create a connection to the MongoDB database server
client = pymongo.MongoClient(host='mongodb') # hostname = servicename for docker-compose pipeline

# Create/use a database
db = client.twitter
# equivalent of CREATE DATABASE twitter;

# Define the collection
collection = db.tweets
# equivalent of CREATE TABLE tweets;

fake = Faker()
while True:
    # We create fake tweet using Faker library that we then insert into mongo
    tweet = {'username': fake.name(), 'text': fake.text(), 'data': random.randint(0, 10)}

    # Insert the tweet into the collection
    logging.warning('-----Tweet being written into MongoDB-----')
    logging.warning(tweet)
    collection.insert_one(tweet) #equivalent of INSERT INTO tweet_data VALUES (....);
    logging.warning(str(datetime.now()))
    logging.warning('----------\n')

    time.sleep(3)