from flask import Blueprint

api = Blueprint('api', __name__)

from . import autenticazione, posts, utenti, commenti, errors
