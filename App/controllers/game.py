from App.models import Game
from App.database import db

def NewGame():
    new_game = Game()
    db.session.add(new_game)
    db.session.commit()
    print (new_game)
    print("DODO")
    return new_game