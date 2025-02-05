import flask_sqlalchemy as alchemy
import flask_migrate as fl_mg


db = alchemy.SQLAlchemy()
migrate = fl_mg.Migrate()


class CandidateModel(db.Model):
    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)
    compatibility = db.Column(db.Integer, unique=False, nullable=True)
    sourcing = db.Column(db.String(80), unique=False, nullable=True)
    status = db.Column(db.String(80), unique=False, nullable=True)

