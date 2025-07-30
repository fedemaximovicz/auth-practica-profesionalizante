# Actividad Práctica Profesionalizante: Login con Django
Este repositorio contiene el desarrollo de la actividad de Práctica Profesionalizante, la cual trata de realizar el sistema de autenticación y autorización el cual será utilizado para el proyecto final de la materia Inteligencia Artificial.

Este **NO** es el repositorio en el cual se realizará el proyecto de Inteligencia Artificial.

Debido a que mi proyecto de Inteligencia Artificial tendrá el backend y el frontend separados, este repositorio contiene el sistema de autenticación y autorización del backend.

El backend está hecho con Djangorestframework, como fue indicado por el profesor.

La autenticación y autorización es mediante tokens JWT, utilizando la librería djangorestframework-simplejwt

## Ejecutar el proyecto
1. Clonar el repositorio:
>> git clone https://github.com/fedemaximovicz/auth-practica-profesionalizante.git
>> cd auth-django
2. Crear entorno virtual:
>> python -m venv env
>> env\Scripts\activate (En Windows)
>> source env/bin/activate (En Linux o Mac)
3. Instalar los paquetes: 
>> pip install -r requirements.txt
4. Correr las migraciones:
>> python manage.py makemigrations
>> python manage.py migrate
5. Ejecutar script para agregar unos registros de ejemplo en la base de datos:
>> python manage.py populate_db
6. Iniciar el servidor>
>> python manage.py runserver

## Documentación de la API (con Swagger)
Una vez el server está iniciado, se puede acceder a la documentación interactiva en Swagger accediendo a 
http://localhost:8000/api/schema/swagger-ui/ en el navegador.

Para probar el login y acceder a los recursos de la api realizar el login desde la UI de Swagger o desde tu cliente preferido al endpoint del login con las siguientes credenciales:
http://localhost:8000/api/token/
```json
{
    "username": "admin",
    "password": "test"
}
```
