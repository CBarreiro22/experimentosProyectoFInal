from flask import Blueprint
from flask import request
from ..commands.athlete import Athlete
operations_blueprint = Blueprint('operations', __name__)


@operations_blueprint.route('/usuarios/crear-deportista', methods=['POST'])
def create_athlete():
    body = request.get_json()
    message_error, error_post_service = Athlete.create_athlete(body)
    if error_post_service:
        return message_error, error_post_service
    else:
        return 'deportista creado exitoso', 200


@operations_blueprint.route('/usuarios/health', methods=['GET'])
def check_health():
    return 'ok', 200
