from flask import Flask
from db import db
import models
import resourses as route
import flask_cors as cr
import flask_migrate as mg

app = Flask(__name__)

cr.CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


migrate = mg.Migrate(app, db)

with app.app_context():
    db.create_all()

app.register_blueprint(route.candidate_blp)
app.register_blueprint(route.excel_blp)
app.register_blueprint(route.csv_blp)
app.register_blueprint(route.pdf_blp)
