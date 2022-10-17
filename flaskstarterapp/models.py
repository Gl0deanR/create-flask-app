from flaskstarterapp import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Users Model
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    last_name = db.Column(db.String(300), nullable=False)
    first_name = db.Column(db.String(300), nullable=False)
    email_address = db.Column(db.String(220), nullable=False, unique=True)

    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('Can\'t see the password.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def serialize_sql(self):
        user_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        user_dict.pop('password_hash')
        user_dict.pop('email_address')
        return user_dict
