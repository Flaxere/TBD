import random
from App.database import db
class Game(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  code = db.Column(db.String(4), nullable=False)
  
  def __init__(self, code):
    self.code = generate_code()
   
  def __repr__(self):
    return f'<Game {self.id} {self.code}>'

  def in_string(self,string,char):
    for ch in string:
       if char == ch:
           return True
    return False

  def generate_code(self):
     string = ""
     for i in range(4):
       char = random.choice(string.digits)
       while in_string(string,char) == True:
          char = random.choice(string.digits)
       string += char
       in_string(string,char)
     return string

 