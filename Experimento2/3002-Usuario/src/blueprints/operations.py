from functools import wraps

from flask import Blueprint, jsonify
from flask import request

from ..commands.partner_service import PartnerService
from ..models.model import init_db, db_session
from ..models.partner import PartnerJsonSchema, Partner

operations_blueprint = Blueprint('operations', __name__)
init_db()
partner_schema = PartnerJsonSchema()

@operations_blueprint.route('/usuarios/consultar-servicios', methods=['GET'])
def consultar_estatus_microservicios():
    result = [partner_schema.dump(r) for r in db_session.query(Partner).all()]
    return jsonify(result), 200

@operations_blueprint.route('/usuarios/crear-servicio', methods=['POST'])
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
