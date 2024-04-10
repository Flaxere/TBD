from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (
    create_game_session,
    jwt_required
)

user_game_views = Blueprint('user_game_views', __name__, template_folder='../templates')

@user_game_views.route('/usergame/play/<int:game_id>', methods=['GET'])
@jwt_required()
def get_game_session(game_id):
   
    session = create_game_session(jwt_current_user.id,game_id)

    return render_template('game_session.html',game = session)

@user_game_views.route('/usergame/play/guess', methods = ['POST'])
@jwt_required()
def game_guess():
    data = request.form
    i =0
    for i in range(4):

        print(data[f'n{i}'])
    return redirect(request.referrer)