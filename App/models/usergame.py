from App.database import db

class UserGame(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
  guesses = db.Column(db.Integer, nullable = False)
  completed = db.Column(db.Boolean,default = False)
  game = db.relationship('Game')
  
  
  def __init__(self, user_id, game_id):
    self.user_id = user_id
    self.game_id = game_id
    self.guesses = 0
    