from App.models import Game
from App.database import db

def create_game():
    new_game = Game()
    db.session.add(new_game)
    db.session.commit()
    print (new_game)
    print("DODO")
    return new_game

def get_game_count():
    game_count = Game.query.count()
    print(game_count)
    return game_count

