from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composer.company.create_view_composer import company_create_view_composer
from src.main.composer.company.list_all_view_composer import company_list_all_view_composer
from src.main.composer.company.report_view_composer import company_gen_report_view_composer
from src.main.composer.company.withdraw_view_composer import company_withdraw_view_composer

company_route_bp = Blueprint("companies_routes", __name__)

@company_route_bp.route("/companies", methods=["POST"])
def create_customer():
    http_request = HttpRequest(body=request.json)
    view = company_create_view_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@company_route_bp.route("/companies", methods=["GET"])
def list_all_customers():
    http_request = HttpRequest()
    view = company_list_all_view_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@company_route_bp.route("/companies/<customer_id>/report", methods=["GET"])
def generate_report(customer_id):
    http_request = HttpRequest(param={ "customer_id": customer_id })
    view = company_gen_report_view_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@company_route_bp.route("/companies/<customer_id>/withdraw", methods=["POST"])
def withdraw(customer_id):
    http_request = HttpRequest(body=request.json, param={ "customer_id": customer_id })
    view = company_withdraw_view_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
