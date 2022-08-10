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
# OR
# MySQL Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/database_name'

# SQL Alchemy Settings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Secret Key
app.config['SECRET_KEY'] = "your_secret_key"

# Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)


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
# from flaskstarterapp.models import Users
from flaskstarterapp.dashboard.dashboard import dashboard

app.register_blueprint(dashboard)
