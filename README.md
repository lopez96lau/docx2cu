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
Las técnicas de modelado en Ingeniería de Software permiten representar un sistema mediante notaciones gráficas, lo que reduce el nivel de abstracción y mejora su comprensión. Cada modelo presenta una perspectiva diferente del sistema a desarrollar. Uno de los más utilizados es el diagrama de casos de uso. Éstos son utilizados para describir las interacciones entre el sistema y su entorno, identificando los actores principales, relaciones y escenarios. La generación de este modelo es fundamental para la fase de diseño del software y requiere de una correcta comprensión del dominio donde estará inmerso el sistema y de las declaraciones de requisitos obtenidas de los stakeholders. Considerando este contexto, en este trabajo se propone el desarrollo de una herramienta para derivar de forma semi-automática los elementos que conforman los diagramas de caso de uso, a partir del análisis de las declaraciones expresadas en lenguaje natural, obtenidas de las tareas de educción, aplicando de técnicas de minería de textos. Esta propuesta tiene por objetivo ser implementada a futuro como un microservicio de un sistema recomendador, e integrada al conjunto de funcionalidades ofrecidas.

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
