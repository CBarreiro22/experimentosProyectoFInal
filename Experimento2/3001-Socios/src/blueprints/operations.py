from dotenv import load_dotenv
from flask import Blueprint

loaded = load_dotenv('.env.development')
operations_blueprint = Blueprint('operations', __name__)


@operations_blueprint.route('/socios/health', methods=['GET'])
def check_health():
    return 'ok', 200
