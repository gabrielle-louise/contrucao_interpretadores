#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Como fazer a atividade:
criar um algoritmo que possa validar expressões de logica proposital escritas em latex e definir se as expressões estão gramaticalmente corretas(validar apenas a forma da expressão, ou seja, a sintaxe)

Formula=Constante|Proposicao|FormulaUnaria|FormulaBinaria.  
Constante="T"|"F". 
Proposicao=[a−z0−9]+ 
FormulaUnaria=AbreParen OperadorUnario Formula FechaParen 
FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen 
AbreParen="(" 
FechaParen=")" 
OperatorUnario="¬" 
OperatorBinario="∨"|"∧"|"→"|"↔" 

expressões validas:
FormulaUnaria=AbreParen OperadorUnario Formula FechaParen
FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen 

Se a expressão não estiver nesses padrões ela não será valida
exemplo: 
FormulaUnaria= OperadorUnario AbreParen Formula FechaParen
'''
constante = ['V','F'] 
for x in constante:
  modelounario = ('$$\\left( \\neg'+ constante[x] +'\\right)')
  if constante[x] == "V":
    print("ok")
  else:
    print("F")

estado = 0
def formulaUnaria(modelounario, i):
  if(i == len(modelounario)):
    print(modelounario + " pertence ")
  else:
    if modelounario[i] == 'b':
      formulaUnaria(modelounario, i + 1)
      print("caiu aqui")

  
#função para abrir um arquivo
with open ("text.txt", "r") as arquivo:
  conteudo = arquivo.readlines() #readlines deixa os dados em lista
  
conteudo = [x.rstrip('\n') for x in conteudo] 
conteudo.pop(0)
print(conteudo)
for elemento in conteudo:
  estado = 0
  formulaUnaria(elemento, 0)
  

