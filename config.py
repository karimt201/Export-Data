import os


class LocalTestingConfig:
    """
    testing configurations for local testing
    """
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
