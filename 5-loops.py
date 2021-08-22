# Range
# Da onde quero começar 
# Até onde quero ir
# De quanto em quanto quero iterar
# Vai percorrer do 1 até 5 
for i  in (range(1,6,1)):
    print (i)

print("-------------------")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in lista:
    print (i) 

print("-------------------")

index = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for key, value in enumerate(lista):
    print('Chave: {k} => Valor: {v}'.format(k=key, v=value))

print("-------------------")

list = {
    "nome": "Paulo",
    "sobrenome": "Rogerio",
    "idade": 39,
    "profissao": "Analista de Sistemas"
} 

for i in list:
    print (i)

print("-------------------")

for i in list.values():
    print(i)

print("-------------------")

for key, value in list.items():
    print('Chave: {k} => Valor: {v}'.format(k=key, v=value))

print("-------------------")

index = 0
while index < 10:
    print (index)
    index += 1
