#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

Meu entendimento para este exercício foi de ler um arquivo, guardar todas as palavras em um dicionário
depois a partir da 1a palavra, escolher um valor aleatorio entre 0 e a maior chave
Então repetir 200 vezes o seguinte:
    Imprime o value correspondente à essa chave aleatória
    Escolher um novo valor aleatório entre a chave atual e a maior chave, sendo que
        caso esse valor seja igual a maior chave, retorna para a chave 0
"""

import random
import sys

def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  vetor = ['']
  arquivo = open(filename)          #Abro o arquivo
  for linha in arquivo.readlines():
      if (len(linha) > 1):
          vetor += linha.split()    #popula vetor com as palavras do arquivo
  arquivo.close()                   #Fecha o arquivo
  return dict(enumerate(vetor))     #retorna um dicionario

def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    aleatorio = 0
    #Pega o valor da chave referente ao value informado na variavel word
    chave = list(mimic_dict.keys())[list(mimic_dict.values()).index(word)]
    for i in range(0, 200):
        #A variavel aleatorio é preenchida com um valor randomico entre a chave e o numero máximo da chave, caso o valor retornado
        # para variavel seja igual ao número máximo da chave, ou seja, chegou ao final, retorna 0, para voltar para o inicio.
        aleatorio = random.randint(chave, len(mimic_dict)) if aleatorio == len(mimic_dict) else random.randint(0, len(mimic_dict))
        print (mimic_dict.get(aleatorio))   #print o value correspondente da chave
        chave = aleatorio
    return

# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
