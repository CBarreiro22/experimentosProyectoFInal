from functools import wraps

from flask import Blueprint
from flask import request

from ..commands.partner_service import PartnerService

operations_blueprint = Blueprint('operations', __name__)


# def validate_request_body(func):
#     @wraps(func)
#     def decorated(*args, **kwargs):
#         json_data = request.get_json()
#         required_fields = ['description', 'size', 'fragile', 'offer']
#         for field in required_fields:
#             if field not in json_data or json_data[field] is None:
#                 return '', 400
#         return func(*args, **kwargs)
#
#     return decorated


@operations_blueprint.route('/usuarios/crear-servicio', methods=['POST'])
# @validate_request_body
def create_partner_service():
    body = request.get_json()
    message_error, error_post_service = PartnerService.create_partner_service(body)
    if error_post_service:
        return message_error, error_post_service
    else:
        return 'servicio creado exitoso', 200


@operations_blueprint.route('/usuarios/health', methods=['GET'])
def check_health():
    return 'pong', 200
