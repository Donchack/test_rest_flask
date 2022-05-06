import os


app_dir = os.path.abspath(os.path.dirname(__file__))
login_date = {
        'lar_nout':
            {
                'login':'postgres',
                'password':'P0rt0k#1'
            },
        'my_comp':
            {

            }
}
the_login = login_date['lar_nout']
DB_URI = {
        'mysql_uri':
        'mysql+pymysql://root:P0rt0k#1@localhost/quiz_quest',
        'postgre_uri':
        f'postgresql://{the_login["login"]}:{the_login["password"]}@localhost:5432/quiz_quest'
}

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'A SECRET KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = '127.0.0.1:5001'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
            'DEVELOPMENT_DATABASE_URI',
            DB_URI['postgre_uri']
    )


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
            'TESTING_DATABASE_URI',
			DB_URI['postgre_uri']
    )


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
            'PRODUCTION_DATABASE_URI',
	        DB_URI['postgre_uri']
    )
