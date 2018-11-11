### Instalación y configuración de Heroku:

Primeramente necesitamos tener Heroku en nuestra máquina, para ello escribimos desde la terminal:
~~~~
sudo snap install heroku --classic
~~~~

Una vez instalado nos logueamos en Heroku mediante:
~~~~
heroku login
~~~~
Nos pedira nuestro usuario y contraseña con el que nos hemos registrado en la página.

Una vez nos encontramos logueados preparamos la aplicación, para ello clonamos el repositorio(desde Git Hub) deseado donde tenemos los archivos de la aplicación en nuestra maquina(en mi caso sería) :
~~~~
git clone https://github.com/JotaGalera/FindAInformatic
~~~~

Ahora nos movemos a ese repositorio:
~~~~
cd FindAInformatic
~~~~


Ejecutamos la orden(en el repositorio correspondiente, en la máquina local):
~~~~
heroku create
~~~~

![](./imgs/heroku-create.png)

De esta manera se creará la aplicación en Heroku asociada a nuestro repositorio con un nombre provisional.
Acto seguido Heroku detecta el lenguaje en que esta escrita la aplicación, en mi caso Python-3.6.6, pip(administrador de paquetes de sistema) utilizado con Python. También reconoce el fichero "Requiremenets" del repositorio e instala los requisitos que nosotros mismos necesitemos para la aplicación.

El nombre de la aplicación en Heroku es aleatorio, pero podemos cambiarlo para que sea más claro mediante la orden:
~~~~
heroku apps:rename "nuevo-nombre"
~~~~

![](./imgs/heroku-new-name.png)


////
Dentro de Heroku en la pestaña Deploy, debemos tener activado el apartado "App connected to GitHub" y "Automatic deploys", de esta manera basta con hacer push sobre el propio repositorio para realizar una actualización y despliegue automático de nuestra aplicación:

![](./imgs/deployment-method.png)

***NOTA***: Marcar la casilla de "Wait for CI to pass before deploy". De esta manera hasta que no pase el test de Travis, no se desplegará la aplicación.

////











Nuestra aplicación ya está desplegada- Nos aseguramos que al menos una instancia de esta se está ejecutando(Para llegar hasta aquí hace falta tener un archivo llamado "Procfile para asignar los dinos, sino nos dará un error el cual se resuelve una vez añadido dicho archivo"):
~~~~
heroku ps:scale web=1
~~~~

![](./imgs/heroku-ps.png)
~~~~
Contenido del archivo "Procfile":

web: gunicorn application:app
~~~~

Y mediante el comando siguiente , podemos abrir nuestra aplicación web:
~~~~
heroku open
~~~~

![](./imgs/heroku-open.png)
