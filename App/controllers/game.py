from App.models import Game
from App.database import db
from datetime import datetime

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

def get_game(id):
    game = Game.query.get(id)
    return game

def isExpired(id):
    game = get_game(id)
    d1 = game.date_created.replace(hour=0, minute=0, second=0, microsecond=0)
    date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    if get_difference(d1,date) >= 1:
        create_game()
        return True 
    return False

def get_difference(date1, date2):
    delta = date2 - date1

    return delta.days

