from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composer.individual.create_view_composer import individual_create_view_composer
from src.main.composer.individual.list_all_view_composer import individual_list_all_view_composer
from src.main.composer.individual.report_view_composer import individual_gen_report_view_composer
from src.main.composer.individual.withdraw_view_composer import individual_withdraw_view_composer

individual_route_bp = Blueprint("individuals_routes", __name__)

@individual_route_bp.route("/individuals", methods=["POST"])
def create_customer():
    http_request = HttpRequest(body=request.json)
    view = individual_create_view_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@individual_route_bp.route("/individuals", methods=["GET"])
def list_all_customers():
    http_request = HttpRequest()
    view = individual_list_all_view_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@individual_route_bp.route("/individuals/<customer_id>/report", methods=["GET"])
def generate_report(customer_id):
    http_request = HttpRequest(param={ "customer_id": customer_id })
    view = individual_gen_report_view_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@individual_route_bp.route("/individuals/<customer_id>/withdraw", methods=["POST"])
def withdraw(customer_id):
    http_request = HttpRequest(body=request.json, param={ "customer_id": customer_id })
    view = individual_withdraw_view_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
