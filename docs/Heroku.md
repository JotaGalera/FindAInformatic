***Desplegamos ahora la aplicación*** en Heroku.
Ejecutamos la orden(en el repositorio correspondiente, en la máquina local):
~~~~
heroku create
~~~~
Se creará un git remoto(llamado Heroku), el cual estará asociado al repositorio local de git.
El nombre de la aplicación en Heroku es aleatorio, pero podemos cambiarlo para que sea más claro mediante la orden:
~~~~
heroku apps:rename "nuevo-nombre"
~~~~
Heroku no permite letras mayucas, espacios, barras bajas, etc. Hay que tenerlo en cuenta a la hora de cambiar el nombre. Una vez lo cambies puedes comprobar que el cambio se ha producido en la misma página(Aunque en la terminar te lo diga también).

Ahora desplegamos el código en Heroku:
~~~~
git push heroku master
~~~~

Acto seguido Heroku detecta el lenguaje en que esta escrita la aplicación, en mi caso Python-3.6.6, pip(administrador de paquetes de sistema) utilizado con Python. También reconoce el fichero "Requiremenets" del repositorio e instala los requisitos que nosotros mismos necesitemos para la aplicación.

Nuestra aplicación ya está desplegada- Nos aseguramos que al menos una instancia de esta se está ejecutando(Para llegar hasta aquí hace falta tener un archivo llamdo "Procfile para asignar los dinos, sino nos dará un error el cual se resulve una vez añadido dicho archivo"):
~~~~
heroku ps:scale web=1
~~~~
