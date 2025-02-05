import os

from flask import Flask
import models
import routes as route
import flask_cors as cr
import config as configurations


app = Flask(__name__)

app.config.from_object(configurations.LocalTestingConfig)
cr.CORS(app)

models.db.init_app(app)
models.migrate.init_app(app, models.db)
with app.app_context():
    models.db.create_all()


app.register_blueprint(route.candidate_blp)
app.register_blueprint(route.excel_blp)
app.register_blueprint(route.csv_blp)
app.register_blueprint(route.pdf_blp)


if __name__ == "__main__":
    app.run()
