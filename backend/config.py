wsgi_app="app:app"
errorlog="error.log"
workers=4
bind=["0.0.0.0:80"]

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'ziqingyu'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'invitation_junnuo'

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
