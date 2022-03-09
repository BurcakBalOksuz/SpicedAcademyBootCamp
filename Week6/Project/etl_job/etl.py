import logging
import time
from sqlalchemy import create_engine
import pymongo
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# creating a vader sentiment analyzer
s  = SentimentIntensityAnalyzer()


mentions_regex= '@[A-Za-z0-9]+'
url_regex='https?:\/\/\S+' #this will not catch all possible URLs
hashtag_regex= '#'
rt_regex= 'RT\s'

def clean_tweet(tweet):
    tweet = re.sub(mentions_regex, '', tweet)  #removes @mentions
    tweet = re.sub(hashtag_regex, '', tweet) #removes hashtag symbol
    tweet = re.sub(rt_regex, '', tweet) #removes RT to announce retweet
    tweet = re.sub(url_regex, '', tweet) #removes most URLs
    
    return tweet


# Establish a connection to the MongoDB server
mongo_client = pymongo.MongoClient(host="mongodb", port=27017)
db = mongo_client.twitter
#time.sleep(10)

# connecting to postgres
pg = create_engine('postgresql://postgres:1234@postgresdb:5432/tweets', echo=True)

# creating psql-table if necessary
pg.execute('''
    DROP TABLE IF EXISTS tweets;
''')

pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500),
    sentiment NUMERIC
);
''')

#df.to_sql('tweets', pg, if_exists='replace')
    
#reading tweets from mongodb, doing sentiment analysis and inserting tweets to PostgreSQL
docs = db.tweets.find()
for doc in docs:
    text = doc['text']
    clean_text=clean_tweet(text)
    sentiment = s.polarity_scores(clean_text)  # assuming your JSON docs have a text field
    #print(sentiment)
    # replace placeholder from the ETL chapter
    score = sentiment['compound']
    #print('tweet:',text)
    #score = 1.0  # placeholder value
    query = "INSERT INTO tweets VALUES (%s, %s);"
    pg.execute(query, (clean_text, score))    
        
