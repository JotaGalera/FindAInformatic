# Configuración y despliegue de la aplicación en Heroku:

1. Nos registramos en Heroku y realizamos el login.

2. Creamos una nueva aplicación.

![](imgs/crearapp2.png)

3. Añadimos el nombre de la aplicación y la región:

![](imgs/create2.png)

4. Una vez creada la linkeamos con nuestro repositorio:

![](imgs/link2.png)

Además activamos el despliegue automático, de tal manera que nuestra aplicación se actualizará con cada push al repositorio de Git.

![](imgs/despliegue2.png)

Es importante dejar marcada la pestaña "Wait for CI pass before deploy" para seguir manteniendo la Integración continua con Travis.
