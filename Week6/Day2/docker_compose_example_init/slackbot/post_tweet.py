import pyjokes
import requests

webhook_url = (
    "https://hooks.slack.com/services/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"
)

joke = pyjokes.get_joke()

data = {"text": joke}
requests.post(url=webhook_url, json=data)

# 1) connecting to postgres
# this requires us to install sqlalchemy to connect

# 2) querying data from postgres

# 3) posting the data on slack
