from flask import Blueprint, render_template, session
from app.models import Post
from app.db import get_db
from app.utils.auth import login_required

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
@login_required
def dash():
    db = get_db()
    postArr = db.query(Post).filter(Post.user_id == session.get('user_id')).all()
    return render_template('dashboard.html', posts=postArr, loggedIn = session.get('loggedIn'))


@bp.route('/edit/<id>')
@login_required
def edit(id):
    db = get_db()
    currentPost = currentPost = db.query(Post).filter(Post.id == id).one()
    return render_template('edit-post.html', post=currentPost, loggedIn = session.get('loggedIn'))

