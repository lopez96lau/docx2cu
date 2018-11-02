# Modelo de una herramienta para la detección de requerimientos y casos de uso
### Proyecto de Investigación de Beca I+D - Año 2018
#### Universidad Tecnológica Nacional - Facultad Regional Santa Fe - Departamento de Ingeniería en Sistemas de Información

###### Docentes a cargo:
- Dra. Gutíerrez, María de los Milagros
- Dra. Ballejos, Luciana

###### Becarios:
- López, Laureano Gonzalo (lopez96lau@gmail.com)
- Fleitas, Tomás Andrés
- Olivieri, Gustavo
- Roa, Santiago

###### Colaboradores:
- Ing. Domínguez, Martín
- Ing. Gramajo, Guadalupe
- Dra. Ale, Mariel Alejandra

###### Resumen del proyecto:
Hoy en día, es normal ver aplicaciones informáticas que hacen uso de la inteligencia artificial para automatizar ciertas tareas que requieren la supervisión de una persona. En el modelo planteado, se desarrolla una herramienta en Python que utiliza el procesamiento del lenguaje natural como estandarte, para la detección de requermientos funcionales en enunciados alojados en archivos de tipo .DOCX.

Uno de los enfoques que se busca en el proyecto, es orientar dichos requerimientos en el diseño de Diagramas de Casos de Uso, los cuales representan a las relaciones entre los actores y las accciones que se deben desarrollar en tales requerimientos, por lo que nuestro principal desafío es la obtención de de información valiosa para nuestro objetivo, mediante técnicas como NLP y machine learning.

### Herramientas:
- Python 3.x (https://www.python.org/downloads/)

Una vez instalado, se deberán descargar los siguientes módulos:

#### NLTK y algunos corpus útiles
*Natural Language Tool Kit*, biblioteca más utilizada para procesamiento de lenguaje natural. Se descarga e instala desde la consola de Python.
```python
$ python
>>> pip install nltk
>>> import nltk
>>> nltk.download('wordnet')
>>> nltk.download('stopwords')
>>> nltk.download('omw')
>>> from nltk.corpus import wordnet as wn
>>> wn.synsets('bank')[0].lemma_names('spa')
```

#### Python-Docx
Permite la extracción del texto guardado en archivos .DOCX. Se descarga e instala desde la consola de Python.
```python
$ python
>>> pip install python-docx
```

#### Stanford POSTagger
Corpus útil que permite clasificar sintácticamente a las palabras dentro de un texto. Deben descargarse dos archivos comprimidos:
  - Paquete básico del corpus:
  - Paquete en español:
  
Una vez que se haya descargado y descomprimido el zip, hay dos archivos que deben localizarse. El primero está directamente dentro de la carpeta raíz, se llama `stanford-postagger.jar`. El segundo, está dentro de la carpeta `models`, y su nombre es `spanish.tagger`. Para ambos archivos se va a necesitar la ruta completa para usarlos con Python y NLTK.


Ahora que se tienen todas las herramientas necesarias instaladas, podrá proceder a ejecutar el script.

***Aclaración:** En caso de errores, se recomienda revisar las rutas utilizadas en el código fuente de cada archivo.*
