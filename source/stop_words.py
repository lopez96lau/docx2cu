from nltk.corpus import stopwords
from string import punctuation   

NON_WORDS = list(punctuation)
NON_WORDS.extend(['¿', '¡'])
STOP_WORDS = set(stopwords.words('spanish'))
STOP_WORDS.update(NON_WORDS)

'''
Algunas palabras ambiguas del lenguaje español que son importantes para la semantica del texto:
STOP_WORDS.remove('es')
STOP_WORDS.remove('son')
STOP_WORDS.remove('ellos')
STOP_WORDS.remove('él')
STOP_WORDS.remove('ella')
STOP_WORDS.remove('cuando')
STOP_WORDS.remove('haya')
STOP_WORDS.remove('hayan')
STOP_WORDS.remove('hay')
STOP_WORDS.remove('para')
STOP_WORDS.remove('tenga')
STOP_WORDS.remove('tienen')
STOP_WORDS.remove('tiene')
STOP_WORDS.remove('esto')
STOP_WORDS.remove('esta')
STOP_WORDS.remove('estos')
STOP_WORDS.remove('este')
'''