from flask import jsonify, request, g, url_for, current_app
from sqlalchemy import desc,asc

from project import db

from project.corsi.models import Corso
from project.serate.models import Serata

from . import api
from .errors import forbidden
from .decorators import permission_required

@api.route('/corsi/')
def get_corsi():
    page = request.args.get('page', 1, type=int)
    pagination = Corso.query.paginate(
        page, per_page=current_app.config['PBG_CORSI_PER_PAGE'],
        error_out=False)
    corsi = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_corsi', page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_corsi', page=page+1)
    return jsonify({
        'corsi': [c.to_json() for c in corsi],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@api.route('/corsi/<int:id>')
def get_corso(id):
    c = Corso.query.get_or_404(id)
    return jsonify(c.to_json())


@api.route('/corsi/<int:id>/serate/')
def get_serate_corso(id):
    c = Corso.query.get_or_404(id)
    return jsonify({
        'serate': [s.to_json() for s in c.serate]
    })

@api.route('/corsi/<int:id>/tags/')
def get_tags_corso(id):
    c = Corso.query.get_or_404(id)
    return jsonify({
        'tags': [t.to_json() for t in c.tags]
    })