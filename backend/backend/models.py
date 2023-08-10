from backend import db, app


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=True)
    essence = db.Column(db.String(64), nullable=True)
    status = db.Column(db.Boolean, nullable=True)
