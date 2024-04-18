import random
from App.database import db

class Game(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  code = db.Column(db.String(4), nullable=False)
  date_created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
  
  def __init__(self):
    self.code = self.generate_code()
   
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
       char =  str(random.randint(0,9))
       while self.in_string(string,char) == True:
          char =  str(random.randint(0,9))
       string += char
       test = self.in_string(string,char)
       
     return string

 