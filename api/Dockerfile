# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /api
COPY . /api/
RUN pip install -r ./api/requirements.txt
