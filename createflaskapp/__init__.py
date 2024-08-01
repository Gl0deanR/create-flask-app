from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from datetime import date

# Create a Flask Instance
app = Flask(__name__)

# Database settings
# SQLITE Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_name.db'

# SQL Alchemy Settings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Secret Key
app.config['SECRET_KEY'] = 'secret_key12345678'  # Change this to your own secret key

# Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Send information across every blueprint in the app
@app.context_processor
def inject_date():
    return {'date': date.today()}


# Flask Login settings
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login_page'
login_manager.login_message_category = "info"
login_manager.login_message = "You must be logged in to view this page."

# Blueprints Settings
# from createflaskapp.models import Users
from createflaskapp.dashboard.dashboard import dashboard
from createflaskapp.api_v1.api_v1 import api_v1
from createflaskapp.auth.auth import auth

app.register_blueprint(dashboard)
app.register_blueprint(api_v1)
app.register_blueprint(auth)
