# pulling base image (i.e. in this case python vs. 3.8 from dock)
FROM python:3.8 

WORKDIR /app

COPY requirements.txt /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "app.py"]



