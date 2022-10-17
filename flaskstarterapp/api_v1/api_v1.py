from flask import Blueprint, jsonify, request
from flaskstarterapp.models import User
from flaskstarterapp import limiter, db
from flaskstarterapp.config import token_globinary

api_v1 = Blueprint("api_v1", __name__,
                   url_prefix="/api-v1",
                   static_folder="static")


@api_v1.route('/')
@limiter.limit("10/minute")  # max 10 requests per minute
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
    """Delete all users."""

    if request.args.get("token_globinary"):
        if request.args.get("token_globinary") == token_globinary:
            for user in User.query.all():
                if user.id > 2:
                    db.session.delete(user)
            db.session.commit()
            api_v1_response = {
                "success": True,
                "message": "All users deleted",
            }
            return jsonify(api_v1_response)
        else:
            api_v1_response = {
                "success": False,
                "message": "Invalid token",
            }
            return jsonify(api_v1_response)
    else:
        api_v1_response = {
            "success": False,
            "message": "No token provided",
        }
        return jsonify(api_v1_response)
