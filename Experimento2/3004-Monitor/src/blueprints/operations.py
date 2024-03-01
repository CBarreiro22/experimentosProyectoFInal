import os
import threading, time
from flask import Blueprint,jsonify, request
from src.models.model import init_db, reset_db, db_session
from src.models.monitor import MonitorJsonSchema, Monitor
from src.models.microservicio import Microservice
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
    micro_usuarios= Microservice("Usuarios", 5,os.environ["USERS_PATH"])
    micro_socios= Microservice("Socios", 5,os.environ["SOCIOS_PATH"])
    while True:
        print('Monitoreando microservicios...')
        micro_usuarios.check()
        micro_socios.check()
        if micro_usuarios.status == "ERROR":
            db_session.add(Monitor(micro_usuarios.name,"ERROR",1))
            micro_usuarios.reset()
        if micro_socios.status == "ERROR":
            db_session.add(Monitor(micro_socios.name,"ERROR",1))
            micro_socios.reset()
        db_session.commit()
        time.sleep(int(os.environ["MONITOR_POLLING_SECONDS"]))

thread = threading.Thread(target=monitorea_microservicios)
thread.start()