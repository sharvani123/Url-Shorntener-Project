FROM python:3

ENV PYTHONBUFFERED 1

WORKDIR /api

ADD . /api

COPY ./requirements.txt  /api/requirements.txt

RUN pip install -r requirements.txt

COPY . /api

