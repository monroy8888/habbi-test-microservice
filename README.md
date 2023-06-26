### Requerimientos
Habi desea tener dos microservicios. El primero para que los usuarios externos puedan
consultar los inmuebles disponibles almacenados en la base de datos. El segundo para que los
usuarios puedan darle “Me gusta” a un inmueble en específico.

#### Servicio de consulta
- Los usuarios pueden consultar los inmuebles con los estados: “pre_venta”, “en_venta” y
“vendido” (los inmuebles con estados distintos nunca deben ser visibles por el usuario).
- Los usuarios pueden filtrar estos inmuebles por: Año de construcción, Ciudad, Estado.
- Los usuarios pueden aplicar varios filtros en la misma consulta.
- Los usuarios pueden ver la siguiente información del inmueble: Dirección, Ciudad,
Estado, Precio de venta y Descripción.

## HAbbiT - api_habbi

- Es un proyecto con el FrameWork FastApi que facilita la consulta de lo se require, cuenta
con una estructura facil de entender y ordenada.
- Cuenta con una herramienta para dockerizar el microservicio y se ejecute todos los requerimientos
automaticamente
- Cuenta con un archivo "Makefile" el cual permite facilitar los comando a la hora de utilizarlo.

### Structura del Proyecto

```
.
├── Dockerfile
├── Makefile
├── README.md
├── api_habbi
│   ├── __init__.py
│   ├── config
│   │   ├── __init__.py
│   │   └── config.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   └── models.py
│   ├── queries
│   │   ├── __init__.py
│   │   └── queries.py
│   └── routes
│       ├── __init__.py
│       └── routes.py
├── docker-compose.yml
├── poetry.lock
├── pyproject.toml
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_query.py
```

### Structura del Proyecto

- Antes de ejecutar el "make build" hay que configurar el archivo .env y añadir
los campos requeridos para acceder a la base de datos. 

```
$ cd ../HabbiT
$ make build
$ make up
$ make logs
```
- Acceder al : [LOCALHOST](http://localhost:8000/docs)

#### Servicio de “Me gusta”
- Los usuarios pueden darle me gusta a un inmueble en específico y esto debe quedar
registrado en la base de datos.
- Los “Me gusta” son de usuarios registrados, y debe quedar registrado en la base de
datos el histórico de “me gusta” de cada usuario y a cuáles inmuebles.

#### Tablas:
```
+----------------+       +--------------+       +--------------+
|    Usuarios    |       |   Inmuebles  |       |   MeGusta    |
+----------------+       +--------------+       +--------------+
| id_usuario (PK)|       | id_inmueble  |       | id_megusta   |
| nombre         |       | titulo       |       | id_usuario   |
| email          |       | descripcion  |       | id_inmueble  |
| ...            |       | ...          |       | fecha        |
+----------------+       +--------------+       +--------------+
```
- La tabla "Usuarios" representa a los usuarios registrados en el sistema. Cada usuario tiene un identificador único (id_usuario), junto con otros atributos como nombre, email, etc.
- La tabla "Inmuebles" representa los diferentes inmuebles en el sistema. Cada inmueble tiene un identificador único (id_inmueble) y otros atributos como título, descripción, etc.
- La tabla "MeGusta" registra los "Me gusta" de los usuarios hacia los inmuebles. Cada "Me gusta" tiene un identificador único (id_megusta) y está asociado a un usuario específico (id_usuario) y a un inmueble específico (id_inmueble).

#### Relaciones:

- Relación uno a muchos entre la tabla "Usuarios" y la tabla "MeGusta". Un usuario puede tener cero o varios "Me gusta", pero cada "Me gusta" pertenece a un único usuario.
- Relación uno a muchos entre la tabla "Inmuebles" y la tabla "MeGusta". Un inmueble puede recibir cero o varios "Me gusta", pero cada "Me gusta" se refiere a un único inmueble.

### SQL Query
```
CREATE TABLE MeGusta (
  id_megusta INT PRIMARY KEY,
  id_usuario INT,
  id_inmueble INT,
  fecha DATETIME,
  FOREIGN KEY (id_usuario) REFERENCES Usuarios (id_usuario),
  FOREIGN KEY (id_inmueble) REFERENCES Inmuebles (id_inmueble)
);
```
