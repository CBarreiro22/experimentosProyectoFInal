from Experimento1.Deportista.src.models.model import init_db
from flask import Blueprint

athlete_blueprint = Blueprint('athlete', __name__)
init_db()


@athlete_blueprint.route('/athlete', methods=['POST'])
def create_athlete():
    pass
