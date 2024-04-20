from App.database import db
import random 

class UserGame(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
  guesses = db.Column(db.Integer, nullable = False)
  completed = db.Column(db.Boolean,default = False)
  result = db.Column(db.Boolean,default = False)
  bulls = db.Column(db.Integer)
  cows = db.Column(db.Integer)
  attempts = db.Column(db.String(120))
  game = db.relationship('Game')
  insult = db.Column(db.String(120))
  
  def __init__(self, user_id, game_id):
    self.user_id = user_id
    self.game_id = game_id
    self.guesses = 0
    self.bulls = 0
    self.cows = 0
    self. attempts = ""
    self. insult = ""

  def generateInsult(self):
    keyword = [''] * 12
    keyword[0] = "Well that was an uneducated guess"
    keyword[1] = "You are making this too easy for me"
    keyword[2] = "Most definately not psychic"
    keyword[3] = "On my dead homie your next guess is also going to be wrong"
    keyword[4] = "Cmon man you are messing up my parlay"
    keyword[5] = "Try harder"
    keyword[6] = "Is this how dumb humans are?"
    keyword[7] = "Why are you even here?"
    keyword[8] = "SMH MY HEAD MY HEAD"
    keyword[9] = "It hurts"
    keyword[10] = "He needs some milk!! get it bulls AND cows"
    keyword[11] = "Check out terraria!!"

    return keyword[random.randint(0,11)]