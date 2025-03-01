import models
import routes
import flask_cors as cr
import config as configurations
from extensions import app


app.config.from_object(configurations.LocalTestingConfig)
cr.CORS(app)

models.db.init_app(app)

models.migrate.init_app(app, models.db)


with app.app_context():
    models.db.create_all()


app.register_blueprint(routes.candidate_blp)
app.register_blueprint(routes.auth_blp)

if __name__ == "__main__":
    app.run()
