from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composer.individual.create_view_composer import individual_create_view_composer

individual_route_bp = Blueprint("individuals_routes", __name__)

@individual_route_bp.route("/individuals", methods=["POST"])
def create_customer():
    http_request = HttpRequest(body=request.json)
    view = individual_create_view_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
