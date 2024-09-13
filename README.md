## Clonar el proyecto

- hacer una copia del `.env.example` que se llame `.env` y configurarlo acorde a nuestras necesidades.
- Una vez configurado los puertos y demás, correr: `docker compose up --build`
- Verificar que estén corriendo los contenedores con `docker ps`
- Para obtener la IP de la DB, en caso de que no podamos conectar la app de Flask, correr:  
 `docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysql_database `
 - Conectarse a la DB a través de DBeaver y hacer un backup de la DB o cargar info.


 ## A TENER EN CUENTA

 ### Conexión desde DBeaver (host)
Usar localhost porque desde la perspectiva de tu sistema operativo (el host donde está corriendo Docker),
Docker está exponiendo el puerto 3306 (interno de MySQL) en el puerto 3307 del host
(como especificamos en el docker-compose.yml).  Docker redirige las conexiones al puerto 3307 del host
hacia el puerto 3306 del contenedor MySQL.

### Conexión desde Flask (dentro de la red de Docker)
Usar `mysql_db` (nombre del servicio en docker-compose) como host porque, dentro de la red de Docker,
los contenedores se comunican entre sí usando nombres de servicio. Cuando definimos un servicio en docker-compose.yml,
Docker crea automáticamente un DNS interno para que los contenedores puedan referirse entre sí por nombre.

En este caso, el contenedor Flask puede conectarse al contenedor MySQL usando el nombre del
 servicio mysql_db, que es cómo Docker lo resuelve dentro de la red.

Usar el puerto 3306 desde la app porque este es el puerto en el que MySQL está escuchando dentro del contenedor.
Dentro de la red de Docker, no necesitas hacer el mapeo de puertos como en el host, ya que
ambos contenedores (Flask y MySQL) están en la misma red de Docker.

### Resumen
DBeaver (host): Usa localhost y el puerto 3307 porque Docker mapea el puerto del contenedor MySQL (3306)
 al puerto 3307 de tu host.
Flask (contenedor): Usa mysql_db y el puerto 3306 porque, dentro de la red de Docker,
 los contenedores se comunican por el nombre del servicio y usan el puerto interno del contenedor.