
#Pull the official base image
FROM python:3.6-slim-buster

#set the working directory
WORKDIR /usr/src/app

#Set environment variables
ENV FLASK_CONFIG="production"
ENV FLASK_APP="app.py"
ENV TESTING=False
ENV DEBUG=False

#install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

#Copy Project
COPY . /usr/src/app/



