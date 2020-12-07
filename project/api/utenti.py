from flask import jsonify, request, current_app, url_for

from project.utenti.models import Utente
from project.blog.models import Post

from . import api


@api.route('/utenti/<int:id>')
def get_utente(id):
    user = Utente.query.get_or_404(id)
    return jsonify(user.to_json())


@api.route('/utenti/<int:id>/posts/')
def get_posts_utente(id):
    user = Utente.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    pagination = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['PBG_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_posts_utente', id=id, page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_posts_utente', id=id, page=page+1)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })
