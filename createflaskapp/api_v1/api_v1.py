from flask import Blueprint, jsonify

from createflaskapp.models import User

api_v1 = Blueprint("api_v1", __name__,
                   url_prefix="/api-v1",
                   static_folder="static")


@api_v1.route('/')
def home():
    """Main API page."""

    all_users = []
    for user in User.query.all():
        all_users.append(user.serialize_sql())

    api_v1_response = {
        "api_version": "1.0",
        "api_name": "Flask Starter App API",
        "api_description": "This is a Flask Starter App API",
        "db_users": all_users,
    }
    return jsonify(api_v1_response)


@api_v1.route('/delete/all-users')
def delete_all_users():
    """Delete all users. To be implemented in the future."""
    pass
