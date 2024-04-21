from App.models import UserGame
from App.database import db

def create_game_session(userID,gameID):
    old_session = UserGame.query.filter_by(user_id=userID,completed=False).first()
    if(old_session):
        return old_session
    new_session = UserGame(userID,gameID)
    db.session.add(new_session)
    db.session.commit()
    print (new_session)
    print("DODO")
    return new_session

def get_game_session(id,user_id):
    session = UserGame.query.filter_by(id=id,user_id=user_id).first()
    return session
    
def delete_games(id):
    session = UserGame.query.filter_by(user_id=id).all()
    try:
        for s in session:
            db.session.delete(s)
        db.session.commit()
        return True
    except Exception:
        db.session.rollback()
        return False
    
def guess_code(guessed_code,id,):
    uGame = UserGame.query.filter_by(id=id).first()
    bullCows = {
        "Bulls":0,
        "Cows":0
    }

    actualCode = uGame.game.code

    #Calculation of bulls and cows for guess 
    for i in range(4) :
        if guessed_code[i] == actualCode[i]:
            bullCows['Bulls'] = bullCows.get('Bulls') + 1

    for gch in guessed_code :
        for ach in actualCode:
            if gch == ach:
                bullCows['Cows'] = bullCows.get('Cows') + 1


    bullCows['Cows'] = bullCows.get('Cows') -  bullCows.get('Bulls') 

    #Modification of UserGame instance variables
    uGame.guesses +=1

    uGame.bulls = bullCows.get('Bulls') 
    uGame.cows = bullCows.get('Cows')

    uGame.attempts += str(uGame.bulls) + str(uGame.cows) + guessed_code

    if uGame.guesses == 10:
        uGame.completed = True
    #The below snippet checks victory condition
    if(bullCows.get('Bulls') == 4):
        uGame.completed = True
        uGame.result = True
    else:
        uGame.insult=uGame.generateInsult()
        print (uGame.insult)
    db.session.commit()
    return bullCows

def getInsult(id):
    uGame = UserGame.query.filter_by(id=id).first()
    return uGame.insult