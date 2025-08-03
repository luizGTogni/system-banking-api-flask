from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composer.company.create_view_composer import company_create_view_composer

company_route_bp = Blueprint("companies_routes", __name__)

@company_route_bp.route("/companies", methods=["POST"])
def create_customer():
    http_request = HttpRequest(body=request.json)
    view = company_create_view_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
