from flask import Blueprint, render_template
from app.models import Post
from app.db import get_db

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
    return render_template('dashboard.html')


@bp.route('/edit/<id>')
def edit(id):
    db = get_db()
    currentPost = currentPost = db.query(Post).filter(Post.id == id).one()
    return render_template('edit-post.html', post=currentPost)

