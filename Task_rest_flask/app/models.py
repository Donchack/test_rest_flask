from app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_quest = db.Column(db.Integer, index=True)
    question = db.Column(db.String(500), index=True, unique=True)
    answer = db.Column(db.String(100))
    created_at = db.Column(db.String(100))

    def __init(self, the_quest):
        self.id_quest = the_quest.get('id')
        self.question = the_quest.get('question')
        self.answer = the_quest.get('answer')
        self.created_at = the_quest.get('created_at')
    
    def __repr__(self):
        return f'< Questions {self.id_quest}:{self.question} Answer:{self.answer}>'

db.create_all()