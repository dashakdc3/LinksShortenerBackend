FROM python:3.10.2-alpine

WORKDIR /

COPY . .

RUN python -m pip install --upgrade pip && pip install --upgrade setuptools
