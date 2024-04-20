from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (
    create_user,
    get_all_users,
    get_user,
    delete_user,
    delete_games,
    rename_user,
    change_password,
    get_all_users_json,
    login,
    jwt_required
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/signup', methods=['GET'])
def get_user_page():
    return render_template('signup.html')

@user_views.route('/signup', methods=['POST'])
def create_user_action():
    data = request.form
    if data['password'] != data['password2']:
        flash("Please enter the same password")
        return redirect(request.referrer)
    user = create_user(data['username'], data['password'])
    if user:
        flash(f"User {data['username']} created!")
        return redirect(url_for('index_views.index_page'))
    flash(f"The username {data['username']} has already been taken!")
    return redirect(request.referrer)

@user_views.route('/api/users', methods=['GET'])
@jwt_required()
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    user = create_user(data['username'], data['password'])
    return jsonify({'message': f"user {user.username} created with id {user.id}"})

@user_views.route('/static/users', methods=['GET'])
@jwt_required()
def static_user_page():
  return send_from_directory('static', 'static-user.html')

@user_views.route('/settings/<int:id>', methods=['GET'])
@jwt_required()
def settings_page(id):
    user = get_user(id)
    if user!=jwt_current_user:
        flash(f"Invalid User")
        return redirect(url_for('index_views.index_page'))
    return render_template('settings.html',user=user) 

@user_views.route('/deleteAccount/<int:id>', methods=['GET'])
@jwt_required()
def del_user(id):
    if jwt_current_user.id != id:
        flash(f"Invalid User")
        return redirect(url_for('index_views.index_page'))
    user = get_user(id)
    name = user.username
    test = delete_games(id)
   
    if(test):
        test2= delete_user(id)
        flash(f"User {name} deleted...")
    else:
        flash(f"User {name} could not be deleted")
    return redirect(url_for('index_views.index_page'))

@user_views.route('/changeUsername/<int:id>', methods=['POST'])
@jwt_required()
def change_uname(id):
    if jwt_current_user.id != id:
        flash(f"Invalid User")
        return redirect(url_for('index_views.index_page'))
    
    data = request.form
    user = get_user(id)
    prevname = user.username
    test = rename_user(id,data['username'])
    if test:
        flash(f"Username Changed from {prevname} to {user.username}")
    else:
        flash(f"The username {data['username']} has already been taken")
    return redirect(request.referrer)

@user_views.route('/changePassword/<int:id>', methods=['POST'])
@jwt_required()
def change_pass(id):
    if jwt_current_user.id != id:
        flash(f"Invalid User")
        return redirect(url_for('index_views.index_page'))
    
    data = request.form
    if data['password1'] != data['password2']:
        flash("Please enter the same password")
        return redirect(request.referrer)
    
    user = get_user(id)
    test = change_password(id,data['password1'])
    flash(f"Password Updated")
    return redirect(request.referrer)
