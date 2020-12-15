"""
Configurazioni
"""
import os
from pathlib import Path

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)


class Config(object):
    FLASK_CONFIG = os.environ.get("FLASK_CONFIG")
    DEBUG = os.environ.get("DEBUG")
    TEST = os.environ.get("TEST")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "supersupersupersecretkey"

    # Supportata recaptcha v.2
    RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
    # Mail
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.googlemail.com")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", "587"))
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # MAIL_USE da valorizzare in ciascun ambiente in base al mail provider
    # per valorizzare i parametri usati dal modulo Flask-Mail
    # https://pythonhosted.org/Flask-Mail/
    # Es. SSL per account GMAIL
    # Es. TSL per account mailtrap.io - Registrati, utile per i test
    MAIL_USE = os.environ.get("MAIL_USE")
    if (MAIL_USE == "SSL"):
        MAIL_USE_TLS = False
        MAIL_USE_SSL = True
    if (MAIL_USE == "TLS"):
        MAIL_USE_TLS = True
        MAIL_USE_SSL = False

    # Costanti usati nelle mail registrazione utenti
    PBG_MAIL_SUBJECT_PREFIX = "[Python Biella Group]"
    PBG_MAIL_SENDER = "Python Biella Group Admin"

    # Definizione email dell'utente ADMIN iniziale
    PBG_ADMIN = os.environ.get("PBG_ADMIN")

    # Per la paginazione
    PBG_COMMENTS_PER_PAGE = 5
    PBG_POSTS_PER_PAGE = 5
    PBG_SERATE_PER_PAGE = 5
    PBG_CORSI_PER_PAGE = 5
    # Per evitare errore modulo API (AttributeError: 'Request' object has no attribute 'is_xhr')
    # https://stackoverflow.com/a/63974534
    # TODO - Analisi approfondita - Credo dipenda dalla versione di Werkzeug
    JSONIFY_PRETTYPRINT_REGULAR = False

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    # Per Heroku Postgress
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = False


class ProdSqliteConfig(Config):

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        basedir, "data.sqlite"
    ) or os.environ.get("SQLALCHEMY_DATABASE_URI")
    DEBUG = False

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("SQLALCHEMY_DATABASE_URI")
        or "postgresql://pbgadmin:SUPERpswd42..@localhost:5432/pbg"
    )
    DEBUG = True

class DevSqliteConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "devdata.sqlite")
    DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        basedir, "testdata.sqlite"
    )
    # To test configuration usage in unit test
    TESTING = True
    # disabling CSRF protection in the testing conguration
    WTF_CSRF_ENABLED = False
    # test admin
    PBG_ADMIN = "test1@test.it"

config = {
    "development": DevConfig,
    "developmentsqlite": DevSqliteConfig,
    "testing": TestConfig,
    "production": ProdConfig,
    "productionsqlite": ProdSqliteConfig,
    "default": DevConfig,
    "None": DevConfig,
}
