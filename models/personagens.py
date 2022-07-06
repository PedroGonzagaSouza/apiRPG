from unicodedata import name
from db import db

class Personagens(db.Model):
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


    def __init__(
        self,
        id,
        name,
        level,
        hp,
        martial,
        handgun,
        bow,
        rifle,
        smg,
        shotgun,
        sniper,
        white,
        blunt,
        stealth,
        carisma,
        strenght,
        agility,
        dodge,
        insanity,
        dinheiro,
        itens
    )

    def __repr__(self):
        
        return f'Personagens(
        id={self.id},
        name={self.name},
        level={self.level},
        hp={self.hp},
        martial={self.martial},
        handgun={self.handgun},
        bow={self.bow},
        rifle={self.rifle},
        smg={self.smg},
        shotgun={self.shotgun},
        sniper={self.sniper},
        white={self.white},
        blunt={self.blunt},
        stealth={self.stealth},
        carisma={self.carisma},
        strenght={self.strenght},
        agility={self.agility},
        dodge={self.dodge},
        insanity={self.insanity},
        dinheiro={self.dinheiro},
        itens={self.itens}
        )'
    

    def json(self):
        return {
            id,
        'name': self.name,
        'level': self.level,
        'hp': self.hp,
        'martial': self.martial,
        'handgun': self.handgun,
        'bow': self.bow,
        'rifle': self.rifle,
        'smg': self.smg,
        'shotgun': self.shotgun,
        'sniper': self.sniper,
        'white': self.white,
        'blunt': self.blunt,
        'stealth': self.stealth,
        'carisma': self.carisma,
        'strenght': self.strenght,
        'agility': self.agility,
        'dodge': self.dodge,
        'insanity': self.insanity,
        'dinheiro': self.dinheiro,
        'itens': self.itens
        }


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        