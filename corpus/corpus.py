# -*- coding: utf-8 -*-
"""corpus.ipynb

Automatically generated by Colaboratory.

Original file is located at
Link colab:
  https://colab.research.google.com/drive/1OJ_rBTBUQs1H0j-fiP4wvewSOy27JDpf?usp=sharing

# Aluna: Gabrielle Louise Ferreira de Melo

 Sua  tarefa  será  transformar  um  conjunto  de  5  sites,  sobre  o  tema  de  processamento  de linguagem natural em um conjunto de cinco listas distintas de sentenças. Ou seja, você fará uma função  que, usando a biblioteca Beautifull Soap, faça a requisição de uma url, e extrai todas as sentenças desta  url. Duas condições são importantes:

  a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que 
  1000 palavras.  
   b) O texto desta página deverá ser transformado em um array de senteças.  

 Para separar as sentenças você pode usar os sinais de pontuação ou as funções da biblibioteca Spacy. 

 link biblioteca: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
 
link texto1: https://www.ibm.com/cloud/learn/natural-language-processing

link texto2: https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP

link texto3: https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html

link texto4: https://en.wikipedia.org/wiki/Natural_language_processing

link texto5: https://www.futurelearn.com/info/blog/what-is-natural-language-processing-nlp
"""

#bibliotecas
from bs4 import BeautifulSoup
import requests
import spacy

#urls dos sites

url1 = "https://www.ibm.com/cloud/learn/natural-language-processing"
url2 = "https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP"
url3 = "https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html"
url4 = "https://en.wikipedia.org/wiki/Natural_language_processing"
url5 = "https://www.futurelearn.com/info/blog/what-is-natural-language-processing-nlp"

#pegando as informações dos sites
info_url1 = requests.get(url1)
info_url2 = requests.get(url2)
info_url3 = requests.get(url3)
info_url4 = requests.get(url4)
info_url5 = requests.get(url5)

#transformando em html
text_html1 = BeautifulSoup(info_url1.text, 'html.parser') #link1
text_html2 = BeautifulSoup(info_url2.text, 'html.parser') #link2
text_html3 = BeautifulSoup(info_url3.text, 'html.parser') #link3
text_html4 = BeautifulSoup(info_url4.text, 'html.parser') #link4
text_html5 = BeautifulSoup(info_url5.text, 'html.parser') #link5

#imprimir html
#print(text_html1)

#transformando em texto

#print(text_html1.get_text()) #link1

#print(text_html2.get_text()) #link2

#print(text_html3.get_text()) #link3

#print(text_html4.get_text()) #link4

print(text_html5.get_text()) #link5

nlp_model = spacy.load("en_core_web_sm")
#doc = nlp_model("NLP combines computational, linguistics—rule-based? modeling of human language—with statistical, machine learning, and deep learning models. Together, these technologies enable computers to process human language in the form of text or voice data and to ‘understand’ its full meaning, complete with the speaker or writer’s intent and sentiment.")
#sents = list(doc.sents)
#print(sents)

"""#transformando sentenças em listas"""

#link1
doc1 = nlp_model(text_html1.get_text())
print(list(doc1.sents))

#link2
doc2 = nlp_model(text_html2.get_text())
print(list(doc2.sents))

#link3
doc3 = nlp_model(text_html3.get_text())
print(list(doc3.sents))

#link4
doc4 = nlp_model(text_html4.get_text())
print(list(doc4.sents))

#link5
doc5 = nlp_model(text_html5.get_text())
print(list(doc5.sents))
