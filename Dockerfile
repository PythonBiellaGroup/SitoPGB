
#Pull the official base image
FROM python:3.6-slim-buster

#set the working directory
WORKDIR /usr/src/app

#Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

#install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

#Copy Project
COPY . /usr/src/app/

#Entrypoint.sh to run the bash script for db
#remember to set permissions to the file: chmod +x ./entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]



