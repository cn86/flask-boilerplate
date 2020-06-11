import os


class BaseConfig:
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class Development(BaseConfig):
    DEBUG = True
    ENV = 'development'
    SECRET_KEY = 'secret'
    SQLALCHEMY_ECHO = True


class Testing(BaseConfig):
    TESTING = True
    ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL')


class Production(BaseConfig):
    ENV = 'production'
    SECRET_KEY = os.getenv('SECRET_KEY')
