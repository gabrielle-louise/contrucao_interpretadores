# -*- coding: utf-8 -*-
"""matriz_distancia.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QD4Sx-JKazc0os4OdoE4HM0zd563oCql

#Aluna: Gabrielle Louise Ferreira de Melo

##Trabalho: Matriz de Distâncias

O trabalho possui código do corpus, bag of word, IF-IDF e a Matriz de distâncias
a parte do IF-IDF precisou ter alterações para realizar a Matriz de distâncias
"""

# -*- coding: utf-8 -*-
"""bagofwords.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1brIKnFAdLikXJpa7TDqApfdR8TPm6Ahj
# Aluna: Gabrielle Louise Ferreira de Melo
Para conseguir fazer o Bag Of Words, o corpus precisou ser feito alterações para uma nova versão.
"""

import requests
from bs4 import BeautifulSoup
import spacy

from IPython.display import display
import pandas as pd

#funcao para excluir tudo que não é texto do site
def transformtxt(nlp):
  palavras = 0
  paragrafos = []
  for i, j in zip(nlp.find_all('p'), nlp.find_all('li')):
    palavras += len(str(i.get_text()).split(' ') )
    palavras += len(str(j.get_text()).split(' ') )
    paragrafos.append(str(i.get_text()))
    paragrafos.append(str(j.get_text()))
  return paragrafos, palavras

#pegando as informações dos sites
headers = {'user-agent' : 'Mozila/5.0'}

texto = requests.get("https://www.ibm.com/cloud/learn/natural-language-processing", headers = headers)
textos = texto.text

#urls dos sites
url1 = requests.get("https://www.ibm.com/cloud/learn/natural-language-processing", headers = headers)
url2 = requests.get("https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP", headers = headers)
url3 = requests.get("https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html", headers = headers)
url4 = requests.get("https://en.wikipedia.org/wiki/Natural_language_processing", headers = headers)
url5 = requests.get("https://www.futurelearn.com/info/blog/what-is-natural-language-processing-nlp", headers = headers)

#transformando em texto e html
info_url1 = url1.text
text_html1 = BeautifulSoup(info_url1, 'html.parser')

info_url2 = url2.text
text_html2 = BeautifulSoup(info_url2, 'html.parser')

info_url3 = url3.text
text_html3 = BeautifulSoup(info_url3, 'html.parser')

info_url4 = url4.text
text_html4 = BeautifulSoup(info_url4, 'html.parser')

info_url5 = url5.text
text_html5 = BeautifulSoup(info_url5, 'html.parser')

nlp = spacy.load('en_core_web_sm') # Load the English Model

#executa a função para tirar o que não é necessário
site1_texto = transformtxt(text_html1)[0]
print(transformtxt(text_html1)[1])

site2_texto = transformtxt(text_html2)[0]
print(transformtxt(text_html2)[1])

site3_texto = transformtxt(text_html3)[0]
print(transformtxt(text_html3)[1])

site4_texto = transformtxt(text_html4)[0]
print(transformtxt(text_html4)[1])

site5_texto = transformtxt(text_html5)[0]
print(transformtxt(text_html5)[1])

text_sites = [site1_texto, site2_texto, site3_texto, site4_texto, site5_texto]
len(text_sites)

#aqui ele ira gerar uma lista com as sentenças para o corpus
corpus = []
cont = 0
for texto in text_sites:
  for sentencas in texto:
    corpus.append([])
    for sentenca in nlp(sentencas).sents:
      for palavra in nlp(str(sentenca)):
        palavra = str(palavra).replace(" ", "\n")
        if palavra != "":
          corpus[cont].append(palavra)
      corpus.append([])
      cont += 1

corpus

#fazendo o bag of words
bagOfWords = []

for doc in corpus:
  docArray = []
  for sent in doc:
    words = sent.split(" ")
    docArray.append(words)
    bagOfWords.append(docArray)


frequencia = {}

#verifica a frequencia de cada sentença, vai acrescentando +1 sempre que achar um lexema igual
for doc in bagOfWords:
  for sent in doc:
    for words in sent:
      if words != "":
        if words in frequencia.keys():
          frequencia[words] += 1
        else:
          frequencia[words] = 1

frequencia = sorted(frequencia.items(), key=lambda x:x[1])

#gera a tabela para visualizar o bag of words
df = pd.DataFrame(frequencia)
# displaying the DataFrame
display(df)

from collections import defaultdict
import numpy as np
import math

#alteraçoes do bag of words para o TF IDF

corpus = []
cont = 0
for texto in text_sites:
  for sentencas in texto:
    corpus.append([])
    for sentenca in nlp(sentencas).sents:
      for palavra in nlp(str(sentenca)):
        palavra = str(palavra).replace(" ", '')
        if palavra != "" and palavra != '\n':
          corpus[cont].append(palavra)
      if not corpus[cont]:
        corpus.pop(cont)
      corpus.append([])
      cont += 1

cont = 0
for i in range(len(corpus)):
  if len(corpus[cont]) == 0:
    corpus.pop(cont)
  else:
    cont += 1

frases = defaultdict(list)
frases = defaultdict(list)
df = defaultdict(list)
pontuacao = ['.', ':','...', ',', ';', '!', '?', '"', '“', '”', '—', '-','(', ')', ] #variavel acrescentada para tirar pontuações na sentença,
#se for achada alguma pontuação que está no vetor o laço ira remover da lista
for termo in corpus:
  for termo2 in termo:
    if termo2 not in pontuacao:
      if frases[termo2] == []:
        frases[termo2] = [1]
        df[termo2] = [0]
      else:
        frases[termo2][0] += 1
    else:
      termo.remove(termo2)

#verifica a quantidade de frases na sentença, se tiver frases iguais é adicionado +1 e colocado na matriz matrizTermo
# se não é colocado zero no lugar com a função zeros do numpy

matrizTermo = []
quant_palavra = len(frases)
keys = frases.keys()
cont_geral = 0
for termo in corpus:
  matrizTermo.append(np.zeros((quant_palavra,), dtype=int))
  for subtermos in termo:
    if subtermos not in pontuacao:
      cont = 0
      for i in frases:
        if i == subtermos:
          matrizTermo[cont_geral][cont] += 1
          break
        cont+=1
  cont_geral +=1
print("Quantidade de palavras: " , quant_palavra)  

#fazendo o tf
tf = []
print("TF:")
for i in range(len(matrizTermo)):
  tf.append([])
  for j in range(len(matrizTermo[i])):
    tf[i].append(float(matrizTermo[i][j]) / float(len(corpus[i])))
print(tf[0])


#df
for palavra_df in df:
  for documento in corpus:
    for palavra_corpus in documento:
      if palavra_df == palavra_corpus:
        df[palavra_df][0] += 1
        break

#idf
idf = []
print("IDF:")
print(len(corpus))
for i in df:
  idf.append( math.log(len(corpus) / df[i][0]))
print(idf)

#TF-IDF
tf_idf = []
print("TF-IDF:")
for i in range(len(tf)):
  tf_idf.append([])
  for j in range(len(tf[i])):
    tf_idf[i].append(tf[i][j] * idf[j])
tf_idf[1]

"""#Matriz de distâncias"""

#matriz de sentenças
quant_matriz= len(tf_idf)
distancia = np.ones((quant_matriz, quant_matriz))
print("Matriz de dinstancias:")
for i in range(0, quant_matriz - 1):
  for j in range(1, quant_matriz):
    cos_sim = np.dot(tf_idf[i],tf_idf[j])/(np.linalg.norm(tf_idf[i])*np.linalg.norm(tf_idf[j]))
    distancia[i][j] = cos_sim
    distancia[j][i] = cos_sim
print(distancia)