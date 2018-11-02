import stop_words, spacy
from stop_words import STOP_WORDS
from nltk import word_tokenize, sent_tokenize, bigrams, trigrams

# Dado un texto, lo reformatea, tokenizando y borrando las stopwords de cada oracion y luego volviendolas a juntar
def reformatearTexto(texto):
    oraciones = sent_tokenize(texto)
    texto = []
    for o in oraciones:
        palabras = borrarStopwords(word_tokenize(o))
        oracion = ' '.join(palabras)
        texto.append(oracion + '.')
    return texto

# Dada una palabra, determina si la misma es o no una stopword
def esStopword(string):
    if string in STOP_WORDS: return True
    else: return False

# Dada una lista de tokens, borra aquellos que sean stopwords
def borrarStopwords(listaTokens):
    palabrasResultado = []
    for token in listaTokens:
        if token not in STOP_WORDS: palabrasResultado.append(token)
    return palabrasResultado
    
# Dada una etiqueta, define si representa a un actor o no
def esActor(etiqueta):
    if(etiqueta == 'nc0s000' or #Sustantivo comun singular
       etiqueta == 'nc0p000' or #Sustantivo comun plural
       etiqueta == 'dd0000'):   #Determinante demostrativo
       return True

# Dada una etiqueta, define si representa a un rol o no
def esRol(etiqueta):
    if(etiqueta == 'vaif000' or #Verbo auxiliar, modo indicativo, tiempo futuro
       etiqueta == 'vaip000' or #Verbo auxiliar, modo indicativo, tiempo presente
       etiqueta == 'vam0000' or #Verbo auxiliar, modo imperativo
       etiqueta == 'vasp000' or #Verbo auxiliar, modo subjuntivo, tiempo presente
       etiqueta == 'vasi000' or #Verbo auxiliar, modo subjuntivo, tiempo imperfecto
       etiqueta == 'vmif000' or #Verbo principal, modo indicativo, tiempo futuro
       etiqueta == 'vmip000' or #Verbo principal, modo indicativo, tiempo presente
       etiqueta == 'vmis000' or #Verbo principal, modo indicativo, tiempo preterito perfecto
       etiqueta == 'vmm0000' or #Verbo principal, modo imperativo
       etiqueta == 'vmsp000' or #Verbo principal, modo subjuntivo, tiempo presente
       etiqueta == 'vsif000' or #Verbo semiauxiliar, modo indicativo, tiempo futuro
       etiqueta == 'vsip000' or #Verbo semiauxiliar, modo indicativo, tiempo presente
       etiqueta == 'vssf000' or #Verbo semiauxiliar, modo subjuntivo, tiempo futuro
       etiqueta == 'vssp000'):  #Verbo semiauxiliar, modo subjuntivo, tiempo presente
       return True              #Agregar tiempo condicional

# Dada una etiqueta, define si representa a un infinitivo o no
def esInfinitivo(etiqueta):
    if etiqueta == 'vmn0000': return True

# Dada una lista de palabras etiquetads, devuelve los actores que pueden extraerse de ellas
def getActores(palabras_etiquetadas):
    actores = []
    for (p,e) in palabras_etiquetadas:
        if esActor(e): actores.append(p)
    return actores

# Dada una lista de palabras etiquetads, devuelve los roles que pueden extraerse de ellas
def getRoles(palabras_etiquetadas):
    roles = []
    for (p,e) in palabras_etiquetadas:
        if esRol(e): roles.append(p)
    return roles

# Dada una lista de palabras etiquetads, devuelve los infinitivos que pueden extraerse de ellas
def getInfinitivos(palabras_etiquetadas):
    infinitivos = []
    for (p,e) in palabras_etiquetadas:
        if esInfinitivo(e): infinitivos.append(p)
    return infinitivos

# Dada una oracion, devuelve una lista con los bigramas que se forman con las palabras de ella
def getBigramas(oracion):
    return list(bigrams(word_tokenize(oracion)))

# Dada una oracion, devuelve una lista con los trigramas que se forman con las palabras de ella
def getTrigramas(oracion):
    return list(trigrams(word_tokenize(oracion)))

# Dada una oracion y una palabra de un trigrama, devuelve los trigramas adyacentes al trigrama que contiene a la palabra argumento
def getTrigramasConsecutivos(oracion,palabra):
    tris = getTrigramas(oracion)
    consecutivos = []
    for t in tris:
        if palabra in t: consecutivos.append(t)
    return consecutivos

nlp = spacy.load('es_core_news_sm') # Carga de spaCy

# Dada una oracion, devuelve una lista con los posibles sujetos que ella contiene
def getSujetos(oracion):
    sujetos = []
    for token in oracion:
        if token.dep_ == 'nsubj': sujetos.append(token)
    return sujetos

# Dada una oracion, devuelve una lista con los posibles roles que ella contiene
def getInfs(oracion):
    infinitivos = []
    for token in oracion:
        if (token.pos_ == 'VERB') & (token.dep_ == 'acl'): infinitivos.append(token)
    return infinitivos

# Dado un sujeto y una palabra, calcula la similaridad vectorial entre ellas
def precisionSujeto(sujeto, palabra):
    sujeto2 = nlp(palabra)
    similarity = sujeto.similarity(sujeto2)
    return similarity

# Dado un set de sujetos y una lista con los tres sujetos mas repetidos del texto, calcula la precision para obtener los "sujetos candidatos" del texto
def sujetosCandidatos(sujetos,listaSujetos):
    candidatos = []
    for s in sujetos:
        #Se tokeniza cada sujeto y se extrae cada SMF
        suj = nlp(str(s))
        smf1 = str(listaSujetos[0][1])
        smf2 = str(listaSujetos[1][1])
        smf3 = str(listaSujetos[2][1])

        #Se calcula la similitud entre el sujeto y SMF
        prec1 = round(precisionSujeto(suj,smf1),3)
        prec2 = round(precisionSujeto(suj,smf2),3)
        prec3 = round(precisionSujeto(suj,smf3),3)

        #Se calculan estadisticas
        sumaPrecs = round(prec1 + prec2 + prec3,3)
        promedio = sumaPrecs / 3

        #Se filtran los sujetos
        if (prec1 < promedio and 
            prec2 < promedio and 
            prec3 < promedio): sujetos.remove(s)
        else: 
            if sumaPrecs > 1.0 : candidatos.append(s)
    return candidatos

# Dada una oracion, permite extraer tuplas de roles y objetos de ella
def getRolObjeto(oracion):
    rol_objeto = []
    for token in oracion:
        if token.pos_ == 'VERB': rol_objeto.append((token,getProximoObjeto(oracion,token)))
    return rol_objeto

# Dada una oracion y un rol, devuelve un par con el rol y el objeto mas proximo que posee en el texto
def getProximoObjeto(oracion,rol):
    tuplas = []
    i = 0
    objeto = ''
    for token in oracion:
        tuplas.append((token.text,token.pos_,token.dep_))
    
    for tupla in tuplas:
        i = i + 1
        if tupla[0] == rol.text: break
    
    tuplas = tuplas[i:]
    for tupla in tuplas:
        if (tupla[1] == 'NOUN') | (tupla[1] == 'ADJ') | (tupla[2] == 'obj'):
            objeto = nlp(tupla[0])
            break
    return objeto

# Dada una oracion, devuelve los adjetivos de los actores de la misma
def getAdjetivos(oracion):
    adjetivos = []
    for token in oracion:
        if (token.dep_ == 'nmod') | (token.dep_ == 'amod'): adjetivos.append(token)
    return adjetivos 

# Dada una oracion y los sujetos del texto, devuelve la lista final de actores con su respectivo adjetivo
def getSujetoAdjetivo(oracion,sujetos):
    suj_adj = []
    suj_aux = sujetos[:]
    trigramas = getTrigramas(oracion.text)
    tuplas = getTuplas(oracion)
    for tri in trigramas:
        for s in suj_aux:
            if s.text == tri[0]:
                for t in tuplas:
                    if (tri[1] == str(t[0])) & (esAdjetivo(t)): suj_adj.append(primeraMayuscula(tri[0]) + primeraMayuscula(tri[1])) ; suj_aux.remove(s) ; break
                    if (tri[2] == str(t[0])) & (esAdjetivo(t)): suj_adj.append(primeraMayuscula(tri[0]) + primeraMayuscula(tri[2])) ; suj_aux.remove(s) ; break
    return set(suj_adj + list(map(lambda x: primeraMayuscula(str(x)), suj_aux)))

# Dada una palabra, devuelve la misma palabra pero con la primer letra en mayuscula
def primeraMayuscula(string):
    return (string[:1].upper()+string[1:])

# Dada una tupla, permite definir si la misma se trata de un adjetivo o no
def esAdjetivo(tupla):
    if (tupla[2] == 'nmod') | (tupla[2] == 'amod'): return True
    else: return False

# Dada una lista de sujetos y una de roles, arma los requerimientos del texto y los devuelve en una lista nueva
def generarCasosDeUso(sujetos,roles):
    requerimientos = []
    for s in sujetos:
        for r in roles:
            if (str(r[1]).lower() in STOP_WORDS) | (r[1] == ''): requerimientos.append((nlp('*'),r[0],s))
            else: requerimientos.append((s,r[0].lemma_,r[1]))
    return requerimientos

# Dada una lista de requerimientos, limpia aquellos que no son coherentes
def filtrarCasosDeUso(listaCasos):
    for c in listaCasos:
        p0 = nlp(str(c[0]))
        p1 = nlp(str(c[1]))
        p2 = nlp(str(c[2]))
        p4 = nlp(str(c[1]) + ' ' + str(c[2]))
        if (p4.similarity(p0) < 0.8) & (p1.similarity(p2) < 0.8) : listaCasos.remove(c)
    return listaCasos

# Dado un texto, lista los posibles sujetos del mismo y los filtra
def listarSujetos(texto_tokenizado):
    sujetos = []
    for token in texto_tokenizado:
        if (token.is_stop == False  and
            token.dep_ != 'punct'   and
            token.dep_ == 'nsubj')  : sujetos.append(token.text)
    return sujetos

# Dada una oracion, arma una lista con las tuplas formadas por cada palabra, su etiqueta POS y su etiqueta de dependencia
def getTuplas(oracion):
    tuplas = []
    for token in oracion:
        tuplas.append((token.text,token.pos_,token.dep_))
    return tuplas