from App.models import User
from App.database import db

def create_user(username, password):
    
    try:
        newuser = User(username=username, password=password)
        db.session.add(newuser)
        db.session.commit()
        return newuser
    except Exception:
        print("FAILURE")
        db.session.rollback()
        return None

def delete_user(id):
    try:
        user = get_user(id)
        db.session.delete(user)
        db.session.commit()
        return True
    except Exception:
        db.session.rollback()
        return False

def rename_user(id,newName):
    try:
        user = get_user(id)
        user.username = newName
        db.session.commit()
        return True
    except Exception:
        db.session.rollback()
        return False
    
def change_password(id,newPass):
    try:
        user = get_user(id)
        user.set_password(newPass)
        db.session.commit()
        return True
    except Exception:
        db.session.rollback()
        return False
   
def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    
def daily_reset():
    user = User.query.all()
    if user:
        try:
            for u in user:
                u.dailyGame = True
            db.session.commit()
            return True
        except Exception:
            return False
    return False

def daygame_played(id):
    user = get_user(id)
    try:
        user.dailyGame = False
        db.session.commit()
        return True
    except Exception:
        return False
