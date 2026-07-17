"""
Tipo String

Aspas Simples 
Aspas Duplas 
Aspas Simples Triplas
Aspas Duplas Triplas
 
"""

status = 'True'
print(type(status))

print('==================')
print(f'Status: {status}')

nome = "Gina's bar"

print('==================')
print(type(nome))
print(f'Nome: {nome}')


# Quebra de Linha
nome = "Paulo \nRogerio"
print('==================')
print(f'Nome: {nome}')

nome = """
Paulo 
Rogerio
"""
print('==================')
print(f'Nome: {nome}')

#  String NÃO é uma lista, embora elas tenham comportamentos parecidos.
# Consigo acessar via Indice

nome = "Paulo Rogerio"
print('==================')
print(type(nome))

# Slice de String
# Isso aqui nao inclue o indice 3 ( vai do 0 ate o 2 )
print(f'Nome: {nome[0:3]}')
print(f'Nome: {nome[:4]}')

# Vai do primeiro ate o ultimo e inverte 
print(f'Nome: {nome[::-1]}')

for i in nome:
    print(i)

# Split => Transforma em uma Lista de String usando espaco como delimitador    
for i in nome.split():
    print(i)    
