from db import db


class CandidateModel(db.Model):
    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)
    compatibility = db.Column(db.Integer, unique=False, nullable=True)
    sourcing = db.Column(db.String(80), unique=False, nullable=True)
    status = db.Column(db.String(80), unique=False, nullable=True)

    # def __init__(self,data):
    #     self.name = data.get('name')
    #     self.email = data.get('email')
    #     self.compatibility = data.get('compatibility')
    #     self.sourcing = data.get('sourcing')
    #     self.status = data.get('status')

    # @staticmethod
    # def query_all():
    #   with app.app_context():
    #     return CandidateModel.query.all()
