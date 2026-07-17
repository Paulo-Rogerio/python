"""
Tudo qu estudamos em dicionario e valido aqui

Para evitar erro ( KeyError ) , ou seja, quando chave for inexistente , e uma boa usar Default Dict .

Default Dict => Ao criar um dicionário utlizando "Default Dict" , nos informamos um default value, podendo
utilizar um lambda para isso. Esse valor será utilizado sempre que NÂO houver um valor definido .

Para uma chave inexistente, o valor default é assumido.
 
 
Lambdas sao funcoes sem nomes que podem ou não receber parametros de entrada e retorna valores. 

def soma(a, b):
    return a + b
print(soma(10, 5))

#====================

soma = lambda a, b: a + b
print(soma(10, 5))

"""

dicionario = {'curso': 'Python'}
print("====================")
print(dicionario['curso'])

from collections import defaultdict

dicionario = defaultdict(lambda: 0)
# defaultdict(<function <lambda> at 0x7a8f4a22b7f0>, {})
# <function <lambda> at 0x7a8f4a22b7f0> Primeiro elemento e uma tupla
# é um defautdict e está vazio
print("====================")
print(dicionario)

dicionario['curso'] =  'Python'
print("====================")
print(dicionario)

print("====================")
print(dicionario['bacate'])

# defaultdict(<function <lambda> at 0x73c999a9f3d0>, {'curso': 'Python', 'bacate': 0})
# COmo a chave "bacate" e inexistente, ele nao retornou KeyErro, mas colocou    um novo elemento bacate com valor 0
print("====================")
print(dicionario)

