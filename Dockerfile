# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/quizzes

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev libjpeg
RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# copy project
COPY . .
