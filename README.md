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

### Integración Continua

Hemos creado una clase inicial ("Informatic"), con una funcionalidad básica la cual realiza un return de true, esta funcionalidad se utiliza para comprobar el buen funcionamiento de nuestro test a través de Travis-CI. Dicha clase tendrá en un futuro datos de los informáticos que se registren en el sistema, al igual que el resto de funcionalidad de estos en el sistema, como puede ser subir un CV, modificarlo, etc...

Travis-CI ofrece un servicio de ___Integración continua___(Práctica de fusionar las copias de trabajo en un repositorio centarl de forma periódica, tras la cual se ejecutan versiones y pruebas automáticas). Este servicio cuenta con una licencia de software libre y trabaja con Git de una forma sencilla y fácil de utilizar.
