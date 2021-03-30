from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


cors = CORS()
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
migrate = Migrate()
toolbar = DebugToolbarExtension()
