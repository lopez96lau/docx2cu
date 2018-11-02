import frecuencias, filtros, spacy
from frecuencias import *
from filtros import *
from docx import Document

# Se abre el documento y se extraen las palabras
texto = ""
f = open(r'C:\Users\lau_9\Documents\Repos\investigacion\source\data\TextoEjemplo.docx', 'rb')
document = Document(f)
for i in document.paragraphs:
    texto += i.text
f.close()

# Se carga el modulo de spaCy y se procesa el texto. Se obtienen los sujetos más frecuentes y se divide al texto en oraciones
nlp = spacy.load('es_core_news_sm')
texto = nlp(texto)
smf = sujetosMasFrecuentes(listarSujetos(texto))
oraciones = texto.sents

# Se inicializan algunas variables auxiliares que se utilizaran posteriormente
actores_aux = []
casos_aux = []
i = 0

# Se extraen los actores y los requerimientos de cada oracion
for oracion in oraciones:
    sujs_aux = getSujetos(oracion)
    sujs_candidatos = sujetosCandidatos(sujs_aux,smf)
    sujs_finales = getSujetoAdjetivo(oracion,sujs_candidatos)
    roles = getRolObjeto(oracion)
    actores_aux.append(sujs_finales)

    reqs_aux = generarCasosDeUso(sujs_finales,roles)
    reqs_finales = filtrarCasosDeUso(reqs_aux)
    casos_aux.append(reqs_finales)

# Se genera un set con todos los actores del documento
actores = set([])
for acs in actores_aux:
    for a in acs: actores.add(a)
actores = sorted(actores)

# Se genera un set con todos los requerimientos del documento
casos = set([])
for caso in casos_aux:
    for c in caso: casos.add(c)

# Se imprimen los resultados
print('\nACTORES DEL TEXTO:\n======================')
for a in actores: print('- ' + a)

print('\nCASOS DE USO DEL TEXTO:\n=============================')
for c in casos: i += 1 ; print(str(i) + '. ' + str(c[0]) + ' -->',primeraMayuscula(str(c[1])),primeraMayuscula(str(c[2])))
print('\n(donde "*" indica que el actor no pudo ser determinado)')

print('\nPRECISION DEL PROGRAMA:\n=======================')
correctos = int(input('Ingrese el número de requerimientos que han sido detectados correctamente, sin incluir Falsos Positivos o Falsos Negativos: '))
precision = round((correctos * 100)/i,3)
print('\n=> Los requerimientos han sido obtenidos con un ' + str(precision) + '%' + ' de precisión.\n')