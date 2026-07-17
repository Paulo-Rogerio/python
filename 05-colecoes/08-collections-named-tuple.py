"""
tupla = (1, 2, 3)
print(tupla[1])

Named Tupla => Tupla nomeada. Sao tuplas diferencias onde especificamos nome e tambem parametros.
"""

from collections import namedtuple


# Crie uma variavel cachorro do tipo namedtuple 
# A tupla vai ser chamada de nome_da_tupla e receberá os seguintes parametros ( idade, raca e nome)
# E como se fosse 3 variaveis para esse variavel cachorro.
# As 3 formas abaixo são equivalentes

# Forma 1
# Parametros passado como string
# cachorro e nome da tupla
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2
# Parametros passado como string separados por ,
# cachorro e nome da tupla
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3
# Aqui cria-se uma Lista
# + Clrara para entender.
# Parametros passado como Lista
# cachorro e nome da tupla
# + usual
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Isso permite criar meu tipo de dado personalizado.
# A partir desse tipo de dado posso criar quantas variaveis eu quiser.

# Criando varivel meg do tipo cachorro.
meg = cachorro(idade=2, raca='tomba-lata', nome='meg')

# Forma 1 - Acessando por Index
print("==================")
print(meg[0])

# Forma 2 - Acessando 
print(meg.idade)

print(meg.index('tomba-lata'))
print(meg.count('tomba-lata'))