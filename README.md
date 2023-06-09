﻿# Tercera-pre-entrega-Dieguez
# Tercera Pre entrega del curso de PYTHON / CODERHOUSE

## _README del proyecto_


**El proyecto consiste en la creación de una plataforma web en donde se acceden a diferentes funcionalidades. Se trata de una aplicación web de un instituto de educacion digital, a ser utilizada tanto por estudiantes como profesores del mismo.**

**El desarrollo del proyecto esta realizado con lenguaje python complementado con el framework django (MVC), con el objetivo de facilitar el contenido front-end del mismo.**


Se crea un proyecto *[django-admin startproject]* dentro del cual posteriormente se crea una aplicacion **(appcoder)** *[python manage.py startapp appcoder]* para que el programa sea entendible y facilmente manipulable. Esta ultima se debe agregar en el archivo *settings.py > installed apps*

Dentro del mismo se crean los siguientes modelos:
- cursos
- profesores
- estudiantes
- entregables

Cada uno con su respectiva informacion segun corresponda.

Para cada uno de los modelos se ha definido su estructura, por medio de clases *[class]*.Por ejemplo, para el modelo *"Curso"* se ha definido una estructrura compuesta por *"nombre"* y *"camada"*.

Los modelos posteriormente se transforman en base de datos *[python manage.py makemigrations]* a las cuales se les genera su propia estructura (la gestion de las BBDD se realiza a traves del software DB Browser for SQLite)

Dentro de la aplicacion, se genera el archivo *urls.py* en donde se importan los paths y las vistas generadas *[from appCoder import views]*
Tambien se crea una carpeta de *templates/appcoder* (la subcarpeta es una buena practica para evitar codigos confusos si se agregasen mas aplicaciones al proyecto). A cada uno de los archivos de template para cada una de las urls se le copian archivos .html + css mediante el framework *'Bootstrap'*.
Existe un template "padre" *(base.html)* y templates "hijos" que heredan su estructura (este proceso se realiza mediante bloques).

Cada una de las vistas de la aplicacion posee un formulario para completar datos segun corresponda. los datos viajan al servidor y se guardan en la base de datos (SQLite), pudiendose consultar mdiante una busqueda con form *(ver: /busqueda_camada)*


///
La aplicacion posee un panel de administracion administrado por un **'super usuario'** que lo administra *[python manage.py createsuperuser]*.
