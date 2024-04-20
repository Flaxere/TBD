from App.models import Game
from App.database import db

def create_game():
   
    db.session.commit()
    
    print("DODO")
    return True

def get_game_count():
    game_count = Game.query.count()
    print(game_count)
    return game_count

