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

@user_views.route('/settings', methods=['GET'])
@jwt_required()
def settings_page():
    return render_template('settings.html',user=jwt_current_user) 

@user_views.route('/deleteAccount', methods=['GET'])
@jwt_required()
def del_user():
    name = jwt_current_user.username
    test = delete_games(jwt_current_user.id)
   
    if(test):
        test2= delete_user(jwt_current_user.id)
        flash(f"User {name} deleted...")
    else:
        flash(f"User {name} could not be deleted")
    return redirect(url_for('index_views.index_page'))

@user_views.route('/changeUsername', methods=['POST'])
@jwt_required()
def change_uname():  
    data = request.form
    prevname = jwt_current_user.username
    test = rename_user(jwt_current_user.id,data['username'])
    if test:
        flash(f"Username Changed from {prevname} to {jwt_current_user.username}")
    else:
        flash(f"The username {data['username']} has already been taken")
    return redirect(request.referrer)

@user_views.route('/changePassword', methods=['POST'])
@jwt_required()
def change_pass():
    
    data = request.form
    if data['password1'] != data['password2']:
        flash("Please enter the same password")
        return redirect(request.referrer)
    
    test = change_password(jwt_current_user.id,data['password1'])
    flash(f"Password Updated")
    return redirect(request.referrer)
