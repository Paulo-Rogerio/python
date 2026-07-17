"""
Escopo de variaveis

Variaveis Globais :
Sao reconhecidas em todos o programa.


Variveis  Locais :
Sao reconhecida no bloco que foi declarada.

Python Linguagem de Tipagem dinamica, o tipo de dado é inferido na declaração da variavel
"""

# Variavel novo nao existe, neste escopo
num = 0
if num > 1:
    novo = "Entrei"

print(f'Numero : {novo}')

