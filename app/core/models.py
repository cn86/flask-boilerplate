from core.extensions import db


class Counter(db.Model):
    __tablename__ = 'counters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    count = db.Column(db.Integer, default=0)
    created_on = db.Column(
        db.DateTime, server_default=db.func.now(), nullable=False
    )
    modified_on = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False
    )
