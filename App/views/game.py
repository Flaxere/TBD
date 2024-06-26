from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (
    get_game_count,
    jwt_required
    
)

game_views = Blueprint('game_views', __name__, template_folder='../templates')

@game_views.route('/game', methods=['GET'])
@jwt_required()
def get_game_page():
    count = get_game_count()
    
    return render_template('gamePage.html',gameid = count)
