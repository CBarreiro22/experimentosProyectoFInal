import os
import threading, time
from flask import Blueprint,jsonify
from src.models.model import init_db, reset_db, db_session
from src.models.monitor import MonitorJsonSchema, Monitor
from dotenv import load_dotenv

loaded = load_dotenv('.env.development')
operations_blueprint = Blueprint('operations', __name__)
init_db()
monitor_schema = MonitorJsonSchema()

@operations_blueprint.route('/monitor/health', methods=['GET'])
def health():
    return 'OK', 200

@operations_blueprint.route('/monitor/reset', methods=['POST'])
def reset_database():
    reset_db()
    return 'Todos los datos fueron eliminados', 200

@operations_blueprint.route('/monitor/consultar-estatus-microservicios', methods=['GET'])
def consultar_estatus_microservicios():
    result = [monitor_schema.dump(r) for r in db_session.query(Monitor).all()]
    return jsonify(result), 200

def monitorea_microservicios():
    while True:
        # Aquí podrías realizar algunas verificaciones para determinar
        # el estado de salud de tu aplicación
        # Por ejemplo, podrías verificar la conexión a una base de datos,
        # la disponibilidad de servicios externos, etc.

        # Si todas las comprobaciones son exitosas, devuelve un mensaje de estado OK
        print('Monitoreando microservicios...')

        # Usuarios
        # Socios
        db_session.add(Monitor("Micro2","OK",1))
        db_session.commit()
        time.sleep(int(os.environ["MONITOR_POLLING_SECONDS"]))

thread = threading.Thread(target=monitorea_microservicios)
thread.start()