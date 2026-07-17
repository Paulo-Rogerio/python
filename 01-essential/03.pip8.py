"""
PEP8

[1] - Utilize camel case para classes

class Calculadora:
    pass

class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minúsculo, separado por underline 

def soma():
    pass

def soma_dois_numeros():
    pass
    
[3] - Utilize 4 espacos para identação.

if 'a' in 'banana':
    print('ok')

[4] - Linhas em branco.
- Separar funções e definições de classe com 2 linhas em branco.
- Method dentro de uma mesma classe , devem ser separados com uma unica linha em branco.

[5] Imports
- Imports devem ser feito em linhas separadas.
- Se o import e feito por um from, para pegar 2 ou 3 Objetos , pode ser na mesma linha
- Imports ficam no topo do arquivo, e logo apos os comentarios

import sys
import os
from types import StringType, ListTypes
from types import (
    StringType, 
    ListTypes
)

[6] Espaçoes entre expressões e instruções

Ex: Ok
funcao(algo[1], {outro: 2})
dict['chave'] = lista[indice]


[7] Declaração de variaveis espacadas.

Não faca isso...

x              = '2'
variavel_longa = '1'

[8] Sempre termine uma instrução com uma nova linha.
"""

import types
