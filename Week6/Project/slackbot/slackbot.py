import pyjokes
import requests
import time
from sqlalchemy import create_engine

webhook_url = (
    "'''''"
)

#connectting postgresql
pg = create_engine('postgresql://postgres:1234@postgresdb:5432/tweets', echo=True)


#Select recent one tweet to send Slack Bot

#if __name__ == '__main__':
    #while True:
        #time.sleep(3600) # for slacking every 60 min
select_query = '''SELECT  text, sentiment FROM tweets ORDER BY sentiment DESC LIMIT 1'''
result = pg.execute(select_query).fetchall()
#print("RESULTTT:",result)
message = f':robot_face: New tweet about Berlin with score {result[0][1]} arrived:\n\nTEXT: {result[0][0]}'
data = {'text': message}
print("score:",result[0][1],"---","text:",result[0][0])
requests.post(url=webhook_url, json = data)

