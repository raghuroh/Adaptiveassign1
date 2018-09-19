from flask import Flask
from config import Config
from logging import FileHandler, WARNING
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment



app = Flask(__name__)
file_handler = FileHandler('ERRORLOG.TXT')
file_handler.setLevel(WARNING)
app.logger.addHandler(file_handler)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view='login'
bootstrap = Bootstrap(app)
moment = Moment(app)


import routes, models

