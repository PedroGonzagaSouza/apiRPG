from db import db

class BookModel(db.Model):
    __tablename__ = 'personagem'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    martial = db.Column(db.Integer)
    handgun = db.Column(db.Integer)
    bow = db.Column(db.Integer)
    rifle = db.Column(db.Integer)
    smg = db.Column(db.Integer)
    shotgun = db.Column(db.Integer)
    sniper = db.Column(db.Integer)
    white = db.Column(db.Integer)
    blunt = db.Column(db.Integer)
    stealth = db.Column(db.Integer)
    carisma = db.Column(db.Integer)
    strenght = db.Column(db.Integer)
    agility = db.Column(db.Integer)
    dodge = db.Column(db.Integer)
    insanity = db.Column(db.Integer)
    dinheiro = db.Column(db.Float)
    itens = db.Column(db.String(100))
    