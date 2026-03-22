# Practica 7 - Aplicación Web con Docker y MySQL

## Descripción

Este proyecto consiste en el desarrollo de una aplicación web utilizando Python (Flask) que se conecta a una base de datos MySQL. La aplicación se ejecuta mediante contenedores Docker utilizando Docker Compose, lo que permite una fácil configuración y despliegue del entorno.

## Objetivo

Desarrollar una aplicación web funcional que implemente una arquitectura basada en contenedores, integrando un servidor de aplicación y una base de datos MySQL.

## Características

* Aplicación web desarrollada en Python con Flask
* Conexión a base de datos MySQL
* Registro automático de visitas en la base de datos
* Visualización del número de visitas en tiempo real
* Interfaz web limpia y estructurada
* Implementación con Docker y Docker Compose

## Tecnologías utilizadas

* Python
* Flask
* MySQL
* Docker
* Docker Compose

## Estructura del proyecto

```
practica7-docker-webapp/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
│
└── src/
    ├── app.py
    └── templates/
        └── index.html
```

## Funcionamiento

La aplicación realiza las siguientes acciones:

1. Establece conexión con la base de datos MySQL.
2. Crea una tabla de visitas si no existe.
3. Inserta un registro cada vez que se accede a la página.
4. Consulta el número total de visitas.
5. Muestra la información en la interfaz web.

## Requisitos

* Tener Docker instalado
* Tener Docker Compose disponible

## Ejecución del proyecto

1. Clonar el repositorio:

```
git clone URL_DEL_REPOSITORIO
```

2. Acceder al directorio del proyecto:

```
cd practica7-docker-webapp
```

3. Ejecutar los contenedores:

```
docker-compose up --build
```

4. Acceder desde el navegador:

```
http://localhost:5000
```

## Notas

* El servicio de base de datos MySQL se ejecuta en un contenedor independiente.
* La aplicación se conecta a la base de datos utilizando el nombre del servicio definido en Docker Compose.
* El sistema maneja la creación automática de la tabla necesaria.

## Autor

Keren Almonte

## Asignatura

Práctica de desarrollo de aplicaciones web con Docker

## Profesor

Elvys Cruz
