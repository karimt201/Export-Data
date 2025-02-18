import flask_sqlalchemy as alchemy
import flask_migrate as fl_mg


db = alchemy.SQLAlchemy()
migrate = fl_mg.Migrate()


candidate_skill = db.Table(
    "candidate_skill",
    db.Column("candidate_id", db.Integer, db.ForeignKey("candidates.id"), primary_key=True),
    db.Column("skill_id", db.Integer, db.ForeignKey("skills.id"), primary_key=True)
)


class CandidateModel(db.Model):
    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)
    phone = db.Column(db.String(80), unique=False, nullable=True)
    education= db.relationship("EducationModel",back_populates="candidate", cascade="all, delete-orphan")
    skills= db.relationship("SkillModel",secondary=candidate_skill,back_populates="candidates")
    experience= db.relationship("ExperienceModel",back_populates="candidate", cascade="all, delete-orphan")
    applications= db.relationship("ApplicationModel",back_populates="candidate", cascade="all, delete-orphan")


class SkillModel(db.Model):
    __tablename__ = "skills"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    candidates= db.relationship("CandidateModel",secondary=candidate_skill,back_populates="skills")

class EducationModel(db.Model):
    __tablename__ = "education"

    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(80), unique=False, nullable=False)
    graduation_year = db.Column(db.Integer, unique=False, nullable=False)
    institution = db.Column(db.String(80), unique=False, nullable=False)
    candidate_id = db.Column(db.Integer,db.ForeignKey("candidates.id"),nullable=False)
    candidate= db.relationship("CandidateModel",back_populates="education")

class ExperienceModel(db.Model):
    __tablename__ = "experience"

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(80), unique=False, nullable=False)
    position = db.Column(db.String(80), unique=False, nullable=False)
    start_date = db.Column(db.String(80), unique=False, nullable=False)
    end_date = db.Column(db.String(80), unique=False, nullable=False)
    candidate_id = db.Column(db.Integer,db.ForeignKey("candidates.id"),nullable=False)
    candidate= db.relationship("CandidateModel",back_populates="experience")


class ApplicationModel(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80), unique=False, nullable=False)
    candidate_id = db.Column(db.Integer,db.ForeignKey("candidates.id"),nullable=False)
    candidate= db.relationship("CandidateModel",back_populates="applications")

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

