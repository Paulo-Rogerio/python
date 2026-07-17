"""
A ordem nos dicionarios nao verm organizados
A ordem nao e garantido

Ordem Dict garante a ordem de inserção dos elementos.
"""


dicionario = { 'manga': 1, 'bacate': 2, 'cereja': 3, 'danoninho': 4  }
print("====================")
for chave, valor in dicionario.items():
    print(f'Chave: {chave} - Valor: {valor}')


from collections import OrderedDict

dicionario = OrderedDict({ 'manga': 1, 'bacate': 2, 'cereja': 3, 'danoninho': 4  })
print("====================")
for chave, valor in dicionario.items():
    print(f'Chave: {chave} - Valor: {valor}')

# Para dicionario comum a ordem nao importa
dict_1 = {'a': 1, 'b': 2}
dict_2 = {'b': 2, 'a': 1}

print("====================")
print(dict_1 == dict_2)


# Para orderedDict a ordem faz total diferenca, para serem iguais as ordens tem que ser igual
dict_ord1 = OrderedDict({'a': 1, 'b': 2})
dict_ord2 = OrderedDict({'b': 2, 'a': 1})

print("====================")
print(dict_ord1 == dict_ord2)
