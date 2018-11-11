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
- Como base de datos en un principio pienso utilizar MariaDB(a la espera de un muy posible cambio a otro tipo, a poder ser "no relacional" para aprender a utilizarlas.)
- Como infraestructura virtual utilizaremos Heroku. Ya que nos permitirá trabajar de forma gratuita(550 horas/mes). Heroku trabaja con "Dynos", unos contenedores que nos permiten la virtualización de nuestra aplicación.
- Como herramienta de testeo para python se utilizará Pytest, ya que facilita mucho la ejecución de estos con una simple orden.


### Descripción de la clase e Integración continua

Hemos creado una clase inicial ("Informatic"), con una funcionalidad básica la cual realiza un return de true, esta funcionalidad se utiliza para comprobar el buen funcionamiento de nuestro test a través de Travis-CI. Además en dicha clase contiene los atributos de cada informático, nombre, curriculum y edad. Dicha clase ofrece la funcionalidad de modificar esos datos y/o de mostrarlos. Travis confirma que las funciones de modificación son correctas, mediante la comprobación del cambio y comparación de resultado(test_Status.py).

Travis-CI ofrece un servicio de ___Integración continua___(Práctica de fusionar las copias de trabajo en un repositorio central de forma periódica, tras la cual se ejecutan versiones y pruebas automáticas). Este servicio cuenta con una licencia de software libre y trabaja con Git de una forma sencilla y fácil de utilizar.

### Instalación

Realizar un fork al proyecto, situarse sobre él en el entorno y realizar el comando:
~~~~
pip install -r requirements.txt
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

### Despligue sobre Heroku [![](https://www.herokucdn.com/deploy/button.svg)](https://findainformatic.herokuapp.com/)

La documentación sobre cómo se despliega el proyecto en Heroku se encuentra en:
[Documentación Heroku](https://jotagalera.github.io/FindAInformatic/Heroku)

*  Enlace al despliegue provisional:[Despliegue](https://findainformatic.herokuapp.com/)

*  Reconocimiento de nombre: [/ruta/Javier](https://findainformatic.herokuapp.com/ruta/Javier)

> Cambiando el nombre, "Javier", por cualquier otro lo reconoce.

* Mostrar los datos de un usuario/informáticos (Preestablecido por ahora): [showData](https://findainformatic.herokuapp.com/changeName/NuevoNombre)

> Muestra los datos de un ususario. Actualmente uno predefinido.

* Modificar nombre de un usuario/informático: [changeName/NuevoNombre](https://findainformatic.herokuapp.com/changeName/NuevoNombre)

> Modificando el parámetro "NuevoNombre" en la URL podemos modificar el nombre del usuario.

* Modificar curriculum de un usuario/informático: [changeCv/NuevoCV](https://findainformatic.herokuapp.com/changeCv/NuevoCV)

> Modificando el parámetro "NuevoCV" en la URL podemos modificar el curriculum del ususario.

* Modificar edad de un usuario/informático: [changeAge/NuevaEdad](https://findainformatic.herokuapp.com/changeAge/NuevaEdad)

> Modificando el parámetro "NuevaEdad" en la URL podemos modificar la edad del ususario.
