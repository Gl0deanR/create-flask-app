from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from datetime import date
from createflaskapp.config import db_user, db_password, db_name, secret_key
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Create a Flask Instance
app = Flask(__name__)

# Database settings
# SQLITE Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_name.db'
# OR
# MySQL Database
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@localhost/{db_name}'

# SQL Alchemy Settings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Secret Key
app.config['SECRET_KEY'] = secret_key

# Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Limit API requests
limiter = Limiter(app, key_func=get_remote_address)


# Send information across every blueprint
@app.context_processor
def inject_date():
    return {'date': date.today()}


# Flask Login settings
login_manager = LoginManager(app)
login_manager.login_view = 'dashboard.login_page'
login_manager.login_message_category = "info"
login_manager.login_message = "You must be logged in to view this page."

# Blueprints Settings
# from createflaskapp.models import Users
from createflaskapp.dashboard.dashboard import dashboard
from createflaskapp.api_v1.api_v1 import api_v1

app.register_blueprint(dashboard)
app.register_blueprint(api_v1)
