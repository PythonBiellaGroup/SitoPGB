web: export FLASK_CONFIG="development_sqlite" & export FLASK_APP="app.py" & export DEBUG=True & flask create_db
web: gunicorn app:app
python-3.6.10