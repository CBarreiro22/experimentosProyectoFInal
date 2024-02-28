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
```json
{
    "nombre": "",
    "descripcion": "",
    "precio": 0.00,
    "regionId": "COL|MEX|BRA",
    "paisId": "COL|MEX|BRA",
    "ciudad": "",
    "socioId": 0
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

