#!/bin/sh
#remember to set permissions: chmod +x ./entrypoint.sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python app.py create_db

exec "$@"