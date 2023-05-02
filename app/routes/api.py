import sys
from flask import Blueprint, request, jsonify, session
from app.models import User, Post, Vote, Comment
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db()

    try:
        newUser = User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )

        db.add(newUser)
        db.commit()
    except:
        print(sys.exc_info()[0])
        db.rollback()
        return jsonify(message='Signup failed'), 500

    session.clear()
    session['user_id'] = newUser.id
    session['loggedIn'] = True
    return jsonify(id=newUser.id)

@bp.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    db = get_db()

    try:
        user = db.query(User).filter(User.email == data['email']).one()
        print(sys.exc_info()[0])
    except:
        print(sys.exc_info()[0])
        return jsonify(message = 'Incorrect credentials'), 400
    
    if user.verify_password(data['password']) == False:
        return jsonify(message = 'Incorrect credentials'), 400
    
    session.clear()
    session['user_id'] = user.id
    session['loggedIn'] = True

    return jsonify(id = user.id)

@bp.route('/users/logout', methods=['POST'])
def logout():
    session.clear()
    return '', 204

@bp.route('/comments', method=['POST'])
def comment():
    data = request.get_json()
    db = get_db()

    try:
        newComment = Comment(
            comment_text = data['comment_text'],
            post_id = data['post_id'],
            user_id = session.get('user_id')
        )
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message = 'Comment failed'), 500
