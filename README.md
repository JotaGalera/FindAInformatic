# FindAInformatic

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Build Status](https://travis-ci.org/JotaGalera/FindAInformatic.svg?branch=master)](https://travis-ci.org/JotaGalera/FindAInformatic)


### Breve descripción:
El proyecto consistirá en un servicio web, en el que un cliente podrá contratar para un trabajo a un informático de una lista en función de sus necesidades y/o cualidades(currículum) del informático.

En una base de datos tendremos tanto las distintas empresas, las cuales tendrán su propia identidad dentro del sistema(registro de usuario), como todos los distintos informáticos que estén interesados en estar registrados para una posible contratación.
Las empresas podrán evaluar los currículum de los distintos informáticos, pudiendo así ofrecerles un puesto en sus filas.
Los informáticos podrán crear/modificar su currículum, así como aceptar o denegar cualquier propuesta por parte de una o más empresas.

### Herramientas que se utilizarán en la realización del proyecto:

- Como lenguaje de programación se utilizará Python, es un lenguaje que está muy vivo en estos momentos y me gustaría aprender todo lo que pueda sobre él.
- Se utilizará el framework "Flask" que nos permite crear aplicaciones web rápidamente. Además cuenta con licencia BSD(licencia de software libre permisiva).
- Como infraestructura virtual utilizaremos Heroku. Ya que nos permitirá trabajar de forma gratuita(550 horas/mes). Heroku trabaja con "Dynos", unos contenedores que nos permiten la virtualización de nuestra aplicación.
- Como herramienta de testeo para python se utilizará Pytest, ya que facilita mucho la ejecución de estos con una simple orden.
- Como IaaS se ha considerado finalmente Google Cloud.


### Despligue sobre Heroku [![](https://www.herokucdn.com/deploy/button.svg)](https://findainformatic.herokuapp.com/)

La documentación sobre cómo se despliega el proyecto en Heroku se encuentra en:
[Documentación Heroku](https://jotagalera.github.io/FindAInformatic/Heroku)

*  Enlace al despliegue provisional:[Despliegue](https://findainformatic.herokuapp.com/)

*  Reconocimiento de nombre: [/ruta/Javier](https://findainformatic.herokuapp.com/ruta/Javier)

> Cambiando el nombre, "Javier", por cualquier otro lo reconoce.

* Mostrar los datos de un usuario/informáticos (Preestablecido por ahora): [showData](https://findainformatic.herokuapp.com/showData)

> Muestra los datos de un usuario. Actualmente uno predefinido.

* Modificar nombre de un usuario/informático: [changeName/NuevoNombre](https://findainformatic.herokuapp.com/changeName)

> [METODO POST]Utilizando alguna herramienta como Postman podemos observar el resultado en el cambio de nombre

* Modificar curriculum de un usuario/informático: [changeCv/NuevoCV](https://findainformatic.herokuapp.com/)

> [METODO POST]Utilizando alguna herramienta como Postman podemos observar el cambio en el CV

* Modificar edad de un usuario/informático: [changeAge/NuevaEdad](https://findainformatic.herokuapp.com/)

> [METODO POST]Utilizando alguna herramienta como Postman podemos observar el cambio en la edad.

### Despligue sobre Heroku con contenedores Docker mediante DockerHub[![](https://www.herokucdn.com/deploy/button.svg)](https://docker-findainformatic.herokuapp.com/)

* Documentación sobre Docker:[Docker info](https://jotagalera.github.io/FindAInformatic/Docker)
* Documentación sobre DockerHub:[DockerHub info](https://jotagalera.github.io/FindAInformatic/DockerHub)
* Documentación del despliegue en Heroku con Docker:
* [Enlace a DockerHub](https://hub.docker.com/r/javier1994/findainformatic/)
*  Contenedor: [FindAInformatic](https://docker-findainformatic.herokuapp.com/)

*  Reconocimiento de nombre: [/ruta/Javier](https://docker-findainformatic.herokuapp.com/ruta/Javier)

> Cambiando el nombre, "Javier", por cualquier otro lo reconoce.

* Mostrar los datos de un usuario/informáticos (Preestablecido por ahora): [showData](https://docker-findainformatic.herokuapp.com/showData)

> Muestra los datos de un ususario. Actualmente uno predefinido.

* Modificar nombre de un usuario/informático: [changeName/NuevoNombre](https://docker-findainformatic.herokuapp.com/changeName/)

> [METODO POST]Utilizando alguna herramienta como Postman podemos observar el resultado en el cambio de nombre

* Modificar curriculum de un usuario/informático: [changeCv/NuevoCV](https://docker-findainformatic.herokuapp.com/changeCv/)

> [METODO POST]Utilizando alguna herramienta como Postman podemos observar el cambio en el CV

* Modificar edad de un usuario/informático: [changeAge/NuevaEdad](https://docker-findainformatic.herokuapp.com/changeAge/)

> [METODO POST]Utilizando alguna herramienta como Postman podemos observar el cambio en la edad.

# Despliegue en un IaaS

[Documentación para Iaas](https://jotagalera.github.io/FindAInformatic/IaaS)

Despliegue final: 35.224.37.217
