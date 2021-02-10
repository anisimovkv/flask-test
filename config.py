class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost/flask-test'
    CACHE_TYPE = "simple"
    SQLALCHEMY_ECHO = False
