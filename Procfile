web: export FLASK_CONFIG="developmentsqlite" && export FLASK_APP="app.py" && export DEBUG=True && flask create_db && flask run 
web: gunicorn run:app -b "0.0.0.0:$PORT" -w 3
python-3.6.10