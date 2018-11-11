# Configuración y despliegue de la aplicación en Heroku:

* __Primero:__ Nos registramos en Heroku y realizamos el login.

* __Segundo:__ Creamos una nueva aplicación.

![](imgs/crearapp2.png)

* __Tercero:__ Añadimos el nombre de la aplicación y la región:

![](imgs/create2.png)

* __Cuarto:__ Una vez creada la linkeamos con nuestro repositorio:

![](imgs/link2.png)

Además activamos el despliegue automático, de tal manera que nuestra aplicación se actualizará con cada push al repositorio de Git.

![](imgs/despliegue2.png)

Es importante dejar marcada la pestaña "Wait for CI pass before deploy" para seguir manteniendo la Integración continua con Travis.

* __Quinto:__ Añadimos a nuestro archivo "Requiremenets.txt" la librería Gunicorn, que será utilizada por Heroku para desplegar la aplicación.

* __Sexto:__ Es necesario que nuestra aplicación tenga un archivo llamado "Procfile", este archivo especifica los comandos que son ejecutados por la aplicación de Dynos.
En mi caso el contenido sería:
~~~~
web: gunicorn application:app
~~~~

* __Séptimo:__ Comprobamos que la aplicación funciona:

![https://findainformatic.herokuapp.com/](imgs/resultado2.png)
