# download linux and python
FROM python:3.8

# makes a dir /app and gors there
WORKDIR /app

#adding requirements.txt into container
COPY requirements.txt /app

#install required libraries
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#the first command to be distributed
CMD ["python", "slackbot.py"]