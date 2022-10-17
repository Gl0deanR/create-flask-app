from flask import Blueprint, jsonify, url_for
import os
from flaskstarterapp import limiter

api_v1 = Blueprint("api_v1", __name__,
                   url_prefix="/api-v1",
                   static_folder="static")


@api_v1.route('/')
@limiter.limit("10/minute")  # max 10 requests per minute
def home():
    """Main API page."""
    image_link = os.path.join(os.getcwd(), "flaskstarterapp", "api_v1", "static", "images", "puppy-1.jpg")
    api_v1_response = {
        "api_version": "1.0",
        "api_name": "Flask Starter App API",
        "api_description": "This is a Flask Starter App API",
        "api_image": url_for("api_v1.static", filename="images/puppy-1.jpg"),
    }
    return jsonify(api_v1_response)
