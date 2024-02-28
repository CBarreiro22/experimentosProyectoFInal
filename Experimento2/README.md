# Experimento 02 - David y Benito

https://proyectofinaluno.atlassian.net/browse/PF-51

![Alt text](image.png)

# Puertos:
    3000-API Gateway -> 3000
    3001-Socios      -> 3001
    3002-Usuario     -> 3002
    3003-Sqs         -> 3003
    3004-Monitor     -> 3004

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

