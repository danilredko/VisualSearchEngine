FROM ubuntu:18.04
WORKDIR /usr/src/app

COPY dataset dataset
COPY src src
COPY requirements.txt .
COPY config.json .

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install x11-apps -y
RUN python3 -m pip install --upgrade pip setuptools
RUN pip3 install -r requirements.txt
RUN python3 src/compute_index.py
