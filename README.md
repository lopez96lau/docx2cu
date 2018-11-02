# Un Enfoque semi-automático para generar Diagramas de Casos de Uso aplicando Técnicas de Minería de Textos
### Proyecto de Investigación de Beca I+D - Año 2018
#### Universidad Tecnológica Nacional - Facultad Regional Santa Fe - Departamento de Ingeniería en Sistemas de Información

###### Docentes a cargo:
- Dra. Gutíerrez, María de los Milagros
- Dra. Ballejos, Luciana
- Dra. Ale, Mariel Alejandra

###### Investigadores:
- López, Laureano Gonzalo
- Ing. Gramajo, Guadalupe

###### Resumen del proyecto:
Hoy en día, es normal ver aplicaciones informáticas que hacen uso de la inteligencia artificial para automatizar ciertas tareas que requieren la supervisión de una persona. En el modelo planteado, se desarrolla una herramienta en Python que utiliza el procesamiento del lenguaje natural como estandarte, para la detección de requermientos funcionales en enunciados alojados en archivos de tipo .DOCX.

Uno de los enfoques que se busca en el proyecto, es orientar dichos requerimientos en el diseño de Diagramas de Casos de Uso, los cuales representan a las relaciones entre los actores y las accciones que se deben desarrollar en tales requerimientos, por lo que nuestro principal desafío es la obtención de de información valiosa para nuestro objetivo, mediante técnicas como NLP y machine learning.

### Herramientas:
- Python 3.x (https://www.python.org/downloads/)
- spaCy (https://spacy.io)
- python-docx (https://python-docx.readthedocs.io/en/latest/)

Una vez instalado Python, se deberán descargar los módulos:

#### spaCy y corpus en español
Biblioteca muy potente y robusta utilizada para procesamiento de lenguaje natural, que entre sus corpus posee uno en español basado en AnCora. Se descarga e instala desde la consola de Python.
```python
$ pip install spacy
$ python -m spacy download es_core_web_sm
```

#### Python-Docx
Permite la extracción del texto guardado en archivos .DOCX. Se descarga e instala desde la consola de Python.
```python
$ pip install python-docx
```

Ahora que se tienen todas las herramientas necesarias instaladas, podrá proceder a ejecutar el script.

***Aclaración:** En caso de errores, se recomienda revisar las rutas utilizadas en el código fuente de cada archivo.*
