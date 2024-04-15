from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (
    create_game_session,
    get_game_session,
    guess_code,
    jwt_required
)

user_game_views = Blueprint('user_game_views', __name__, template_folder='../templates')

@user_game_views.route('/start_game/<int:game_id>', methods=['GET'])
@jwt_required()
def start_game_session(game_id):
    session = create_game_session(jwt_current_user.id,game_id)
    
    return redirect(url_for('user_game_views.game_session',game_id=session.id))

@user_game_views.route('/usergame/play/<int:game_id>', methods=['GET'])
@jwt_required()
def game_session(game_id):
    session = get_game_session(game_id)
     
    return render_template('game_session.html',game = session)

@user_game_views.route('/usergame/play/guess/<int:game_id>', methods = ['POST'])
@jwt_required()
def game_guess(game_id):
    data = request.form
    i =0
    str = ""
    for i in range(4):
        str +=data[f'n{i}']
    unique = 0
    for ch in str:
        for i in range(4):
            if(ch == data[f'n{i}']):
                unique +=1
    
    if unique > 4:
        flash("Please enter four unique numbers")
        return redirect(request.referrer)
    bullCows = guess_code(str,game_id)
    if(bullCows.get('Bulls')==4):
        print("victory")
        flash("Victory")
    else:
        flash("Incorrect! Guess again")
    return redirect(request.referrer)