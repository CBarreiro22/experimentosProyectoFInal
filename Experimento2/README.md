# Experimento 02 - David y Benito

https://proyectofinaluno.atlassian.net/browse/PF-51

# Registrar al menos dos servicios de un tercero
- Deportólogo 
- Entrenador 
- Alimentación *
- Transporte *
- Acompañante

# Estructura de datos para el nuevo servicio:
- Payload (IN) - POST
- Nombre del metodo: crear-servicio
```json
{
    "name": "Equipaje seguro",
    "description": "enviar tus implementos de deporte al lugar de entrenamiento seguro",
    "price": 0.00,
    "serviceTypeId": "TRANSPORTE",
    "regionId": "COL",
    "countryId": "COL",
    "city": "BOG",
    "partnerId": 0
}
```
- Response (OUT) - StatusCode: 200: Exitoso, 404:Algun dato no encontrado, 500: Error interno
```json
{
    "mensaje": ""
}
```

# Base de datos
- Tabla monitor
    id
    timestamp
    timestampRecuperacion
    nombreMicroservicio
    estadoMicroservicio
    contador
- Tabla servicios
    id
    nombre
    descripcion
    precio
    tipoServicioId
    regionId
    paisId
    ciudad
    socioId

![Alt text](image.png)

# Postman

# Puertos:
    3000-API Gateway -> 3000 <- TBD
    3001-Socios      -> 3001 <- David
    3002-Usuario     -> 3002 <- David
    3003-Sqs         -> 3003 <- Benito
    3004-Monitor     -> 3004 <- Benito

# Referencia de proyectos 
    https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo11/tree/main

# Instrucciones
1. Para configurar permisos de uso con aws:
    aws configure

2. Para crear entorno virtual
    install --upgrade pip   
    python -m venv virtual   
    source virtual/bin/activate    

3. Para generar requirements
    pip3 freeze > requirements.txt

4. Crea contenedor
    docker build . -t <<nombre contenedor>>

5. Ejecutar contenedor
    docker run <<nombre de contenedor>>  
    docker run -p <<puerto>>:<<puerto>> <<nombre de contenedor>>  
    docker run --env-file .env.development -p <<puerto>>:<<puerto>> <<nombre de contenedor>>  

# Microservicios (local)
    3000-API Gateway
        http://127.0.0.1:3000/gateway/health

    3001-Socios 
        http://127.0.0.1:3001/socios/health
        http://127.0.0.1:3001/socios/reset

    3002-Usuario     
        http://127.0.0.1:3002/usuarios/crear-servicio
        http://127.0.0.1:3002/usuarios/consultar-servicios
        http://127.0.0.1:3002/usuarios/health

    3003-Sqs        
        http://127.0.0.1:3003/sqs/health

    3004-Monitor    
        http://127.0.0.1:3004/monitor/health
        http://127.0.0.1:3004/monitor/reset
        http://127.0.0.1:3004/monitor/consultar-estatus-microservicios

# Microservicios (aws)
    3000-API Gateway
        http://{host-api-gateway}/gateway/health

    3001-Socios
        http://{host-socios}/socios/health
        http://{host-gateway}/socios/reset

    3002-Usuarios    
        http://{host-usuarios}/usuarios/crear-servicio
        http://{host-usuarios}/usuarios/health

    3003-Sqs        
        http://{host-sqs}/health

    3004-Monitor    
        http://{host-monitor}/monitor/health
        http://{host-monitor}/monitor/reset
        http://{host-monitor}/monitor/consultar-estatus-microservicios


# Base de datos Monitor
sudo --login --user=postgres psql

CREATE DATABASE monitordb;
CREATE USER monitoru WITH PASSWORD 'monitorp';
GRANT ALL PRIVILEGES ON DATABASE monitordb TO admin;
\c monitordb  postgres;
GRANT ALL ON SCHEMA public TO monitoru;

drop database monitordb;
drop role monitoru;