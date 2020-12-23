# Creazione dell'immagine docker
################################
# Immagine base di partenza
FROM python:3.6-slim-buster

# Metadati, etichette
LABEL name="pythonbiellagroupsite_docker"
LABEL maintainer="pythonbiellagroup@gmail.com"
LABEL version="1.0"

# Directory di lavoro (se non esiste viene creata)
WORKDIR /usr/src/app

# Variabili di ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN:esecuzione di comandi
# Installazione dipendenze di sistema
RUN apt-get update && apt-get install -y netcat
# Installazione e aggiornamento pip
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
# Installazione dipendenze progetto
RUN pip install -r requirements.txt

# Copia del progetto dal disco a dentro il container
COPY . /usr/src/app/

# Entrypoint.sh to run the bash script for db
# Remember to set permissions to the file: chmod +x ./entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# Verifica valorizzazione variabili di ambiente
RUN echo $FLASK_CONFIG
RUN echo $DB
