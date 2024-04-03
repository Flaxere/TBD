from App.database import db
class Game(db.Model):
  __tablename__ = "game"
  id = db.Column(db.Integer, primary_key=True)
  code = db.Column(db.String(4), nullable=False)
  
  def __init__(self, code):
    self.code = generate_code
   
  def __repr__(self):
    return f'<Game {self.id} {self.code}>'

  def generate_code(self):
     string = ""
     for i in range(4):
       char = random.choice(string.digits)
       while in_string(string,char):
          char = random.choice(string.digits)
       string += char
     return string

  def in_string(self,string,char):
    for ch in string:
       if char == ch:
           return True
    return False