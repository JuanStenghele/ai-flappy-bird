FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./app .
CMD python3 main.py
