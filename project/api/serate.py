from flask import jsonify, request, g, url_for, current_app
from sqlalchemy import desc,asc
import datetime

from project import db

from project.serate.models import Serata

from . import api
from .errors import forbidden
from .decorators import permission_required


@api.route('/prossime-serate/')
def get_prossime_serate():
    page = request.args.get('page', 1, type=int)
    pagination = Serata.query.filter(Serata.data > datetime.datetime.now()).order_by(asc(Serata.data)).paginate(
        page, per_page=current_app.config['PBG_SERATE_PER_PAGE'],
        error_out=False)
    serate = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_prossime_serate', page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_prossime_serate', page=page+1)
    return jsonify({
        'serate': [s.to_json() for s in serate],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })

@api.route('/serate/')
def get_serate():
    page = request.args.get('page', 1, type=int)
    pagination = Serata.query.order_by(desc(Serata.data)).paginate(
        page, per_page=current_app.config['PBG_SERATE_PER_PAGE'],
        error_out=False)
    serate = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_prossime_serate', page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_prossime_serate', page=page+1)
    return jsonify({
        'serate': [s.to_json() for s in serate],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })

@api.route('/serate/<int:id>')
def get_serata(id):
    s = Serata.query.get_or_404(id)
    return jsonify(s.to_json())