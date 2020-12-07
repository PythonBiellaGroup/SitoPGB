from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config
import os

# Per modulo autenticazione Utente
from flask_login import LoginManager

# Per email
from flask_mail import Mail

# Per gestire profilo / now
from flask_moment import Moment

# Per blog
from flask_pagedown import PageDown

# Use bootstrap with the app
bootstrap = Bootstrap()
pagedown = PageDown()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

# Per modulo autenticazione Utente
login_manager = LoginManager()
login_manager.login_view = "auth.login"
# Personalizzazione del messaggio di errore su pagina che richiede autenticazione
login_manager.login_message = "Autenticati per vedere questa pagina"
login_manager.login_message_category = "info"


def create_app():
    FLASK_CONFIG = os.getenv("FLASK_CONFIG", "None")
    print(f"App starting using {FLASK_CONFIG} configuration ")
    app = Flask(__name__, static_folder="static")
    app.config.from_object(config[FLASK_CONFIG])
    config[FLASK_CONFIG].init_app(app)
    bootstrap.init_app(app)
    pagedown.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # Per modulo autenticazione Utente
    login_manager.init_app(app)

    # NOTE! These imports need to come after you've defined db, otherwise you will
    # get errors in your models.py files.
    ## Grab the blueprints from the other routes.py files for each "app"

    # utenti blueprint
    from project.utenti.routes import utenti_blueprint

    app.register_blueprint(
        utenti_blueprint, url_prefix="/utenti", url_static="../static"
    )

    # corsi blueprint
    from project.corsi.routes import corsi_blueprint

    app.register_blueprint(corsi_blueprint, url_prefix="/corsi", url_static="../static")

    # tags blueprint
    from project.tags.routes import tags_blueprint

    app.register_blueprint(tags_blueprint, url_prefix="/tags", url_static="../static")

    # serate blueprint
    from project.serate.routes import serate_blueprint

    app.register_blueprint(
        serate_blueprint, url_prefix="/serate", url_static="../static"
    )

    # blog blueprint
    from project.blog.routes import blog_blueprint

    app.register_blueprint(blog_blueprint, url_prefix="/blog", url_static="../static")

    # commenti blueprint
    from project.commenti.routes import commenti_blueprint

    app.register_blueprint(
        commenti_blueprint, url_prefix="/commenti", url_static="../static"
    )

    # main routes blueprint
    from project.main.routes import main_blueprint

    app.register_blueprint(main_blueprint, url_prefix="/main", url_static="../static")

    # auth blueprint
    from project.auth.routes import auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/auth", url_static="../static")

    # api blueprint
    from project.api import api as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    # error pages blueprint
    from project.error_pages.routes import error_pages_blueprint

    app.register_blueprint(error_pages_blueprint)

    @app.route("/")
    def index():
        return redirect(url_for("main.index"))

    return app
