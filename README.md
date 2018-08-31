# Ripio test

Prueba tecnica de ripio. Márquez Germán

# Puesta en marcha
Basta con ejecutar docker-compose para que los servicios se levanten y el entorno quede operativo.


```sh
$ docker-compose up
```
Se puede parar los contenedores y retomar el estado anterior

Para forzar el build
```sh
$ docker-compose up --build
```

# Estructura
La app esta dividida en 3 servicios que dan soporte a las 3 capas principales de la arq.
- frontend: Implementada en Vuejs usando bootstrap 4
- api: API RestFul implementada en Python3 usando Flask
- mongo: Base de datos utilizada para la solición. 
  
### Pendientes

 - Agregar flask-socketio para dar actualizaciones constante en la vista contra eventos en la api.
 - Agregar más funcionalidad
 - Mejorar backend
 - Mejorar la adminsitración de tokens

License
----

MIT
