#!/bin/sh
#remember to set permissions: chmod +x ./entrypoint.sh

if [ "$DATABASE" = "pbg" ]
then
    echo "Waiting for postgres pbg database..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "Launching creation of db"
flask create_db
echo "DB Creation completed"

exec "$@"