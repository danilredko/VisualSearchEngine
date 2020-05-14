FROM python:3.7-slim
WORKDIR /usr/src/app

COPY dataset dataset
COPY src src
COPY requirements.txt .
COPY config.json .

RUN pip install -r requirements.txt
RUN python compute_index.py
