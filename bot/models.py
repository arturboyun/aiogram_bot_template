from gino import Gino

db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True, index=True)
    user_id = db.Column(db.Integer, unique=True, index=True)
    username = db.Column(db.String(255), default='noname', unique=True, index=True)
    full_name = db.Column(db.String(255), nullable=False)
    tik_tok_id = db.Column(db.Integer, unique=True, index=True)
