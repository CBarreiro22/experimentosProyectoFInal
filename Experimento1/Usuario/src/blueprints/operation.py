from functools import wraps

from flask import Blueprint
from flask import request

from Experimento1.Deportista.src.models.athlete import Athlete

operations_blueprint = Blueprint('operations', __name__)


@operations_blueprint.route('/usuarios/crear-deportista', methods=['POST'])
def create_athlete():
    body = request.get_json()
    message_error, error_post = Athlete.create_athlete(body)
    if error_post:
        return message_error, error_post
    else:
        return 'deportista creado exitosamente', 200
