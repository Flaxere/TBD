from App.models import UserGame
from App.database import db

def create_game_session(userID,gameID):
    new_session = UserGame(userID,gameID)
    db.session.add(new_session)
    db.session.commit()
    print (new_session)
    print("DODO")
    return new_session