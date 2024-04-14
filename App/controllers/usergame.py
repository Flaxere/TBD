from App.models import UserGame
from App.database import db

def create_game_session(userID,gameID):
    old_session = UserGame.query.filter_by(completed=False).first()
    if(old_session):
        return old_session
    new_session = UserGame(userID,gameID)
    db.session.add(new_session)
    db.session.commit()
    print (new_session)
    print("DODO")
    return new_session

def get_game_session(id):
    session = UserGame.query.filter_by(id=id).first()
    return session
    

def guess_code(guessed_code,id,):
    uGame = UserGame.query.filter_by(id=id).first()
    bullCows = {
        "Bulls":0,
        "Cows":0
    }
    actualCode = uGame.game.code

    for i in range(4) :
        if guessed_code[i] == actualCode[i]:
            bullCows['Bulls'] = bullCows.get('Bulls') + 1

    for gch in guessed_code :
        for ach in actualCode:
            if gch == ach:
                bullCows['Cows'] = bullCows.get('Cows') + 1


    bullCows['Cows'] = bullCows.get('Cows') -  bullCows.get('Bulls') 
    uGame.guesses +=1
    if(bullCows.get('Bulls') == 4):
        uGame.completed = True
    db.session.commit()
    return bullCows
