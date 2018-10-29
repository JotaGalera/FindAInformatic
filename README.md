# FindAInformatic

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Build Status](https://travis-ci.org/JotaGalera/FindAInformatic.svg?branch=master)](https://travis-ci.org/JotaGalera/FindAInformatic)

### Breve descripción:
El proyecto consistirá en un servicio web, en el que un cliente podrá contratar para un trabajo a un informático de una lista en función de sus necesidades y/o cualidades(curriculum) del informático.

En una base de datos tendremos tanto las distintas empresas, las cuales tendrán su propia identidad dentro del sistema(registro de usuario), como todos los distintos informáticos que estén interesados en estar registrados para una posible contratación.
Las empresas podrán evaluar los currículum de los distintos informáticos, pudiendo así proponerles un puesto en sus filas.
Los informáticos podrán crear/modificar su currículum, así como aceptar o denegar cualquier propuesta por parte de una o más empresas.

### Herramientas que se utilizarán en la realización del proyecto:

- Como lenguaje de programación se utilizará Python, es un lenguaje que está muy vivo en estos momentos y me gustaría aprender todo lo que pueda sobre él.
- Se utilizará el framework "Flask" que nos permite crear aplicaciones web rápidamente. Además cuenta con licencia BSD(licencia de software libre permisiva).
- Utilizaremos "virtualenv" como entorno virtual para python, es el recomendado para programar en este lenguaje, de esta manera aislaremos el proyecto de nuestro propio sistema.
- Como base de datos en un principio pienso utilizar MariaDB(a la espera de un muy posible cambio a otro tipo, a poder ser "no relacional" para aprender a utilizarlas.)
- Como infraestructura virtual , en un inicio partiremos de intentar utilizar Azure, abierto a cambios futuros.
- Como herramienta de testeo para python se utilizará Pytest, ya que facilita mucho la ejecución de estos con una simple orden.


### Explicación de infraestructura:

Azure permite compilar, implementar y administrar aplicaciones.

Se selecciona la región de los datacenters donde estará tu servicio y el tipo de servicio.
Seleccionas las características(RAM, espacio en disco, ...).

Entre los servicios de Azure se dispone de infraestructuras(como máquinas virtuales, redes, ...) y plataformas. Todo ello con todo tipo de compatibilidad: Linux, Oracle, iOS, Andorid, etc.

### Cómo llebar a cabo dicha infraestructura:

[Guia a la espera de prueba](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal)

### Descripción de la clase e Integración continua

Hemos creado una clase inicial ("Informatic"), con una funcionalidad básica la cual realiza un return de true, esta funcionalidad se utiliza para comprobar el buen funcionamiento de nuestro test a través de Travis-CI. Además en dicha clase contiene los atributos de cada informático, nombre, curriculum y edad. Dicha clase ofrece la funcionalidad de modificar esos datos y/o de mostrarlos. Travis confirma que las funciones de modificación son correctas, mediante la comprobación del cambio y comparación de resultado(test_Status.py).

Travis-CI ofrece un servicio de ___Integración continua___(Práctica de fusionar las copias de trabajo en un repositorio central de forma periódica, tras la cual se ejecutan versiones y pruebas automáticas). Este servicio cuenta con una licencia de software libre y trabaja con Git de una forma sencilla y fácil de utilizar.

### Instalación

Realizar un fork al proyecto, situarse sobre él en el entorno y realizar el comando:
~~~~
pip install -r requeriments.txt
~~~~

### Comprobación de los test

Sobre la raíz del proyecto realizar:
~~~~
pytest
~~~~
o bien:
~~~~
pytest src/test_Status.py
~~~~
Los resultados saldrán inmediatos.

### Arrancar la aplicación

Realizar el comando:

~~~~
python3 mainProject.py
~~~~

### Instalación y configuración de Heroku:

Primeramente necesitamos tener Heroku en nuestra máquina, para ello escribimos desde la terminal:
~~~~
sudo snap install heroku --classic
~~~~

Una vez instalado nos loggeamos en Heroku mediante:
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

Nuestra aplicación ya está desplegada- Nos aseguramos que al menos una instancia de esta se está ejecutando:
~~~~
heroku ps:scale web=1
~~~~
