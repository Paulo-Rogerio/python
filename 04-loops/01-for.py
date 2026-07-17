nome = 'Paulo'
lista = [1, 2, 3, 4, 5]
numeros = range(1, 6)

# for i in nome:
#     print(i)
# print('================')

# Se quiser imprimir tudo em um unica linha?
# Por default o print injeto \n
# for i in nome:
#     print(i, end='')


# Qual index da letra u

# Enumerate
# ((0, 'P'), (1, 'a'), (2, 'u'), (3, 'l'), (4, 'o'))

# Traz a chave e o valor
# for i in enumerate(nome):
#     print(i)
# (0, 'P')
# (1, 'a')
# (2, 'u')
# (3, 'l')
# (4, 'o')

# for k, v in enumerate(nome):
#     print(f'A letra {v} aponta para o index {k}')

# Se tenho 2 valores e quero descartar um.

# for _, i in enumerate(nome):
#     print(i)

# for i in lista:
#     print(i)
# print('================')

# No range o valor final nao e inclusivo 
# Do 1 ate o 9
# for i in numeros:
#     print(i)
# print('================')


# https://apps.timwhitlock.info/emoji/tables/unicode
# U+1F60D
# U0001F60D


for i in range(1, 11):
    print('\U0001F60D' * i)