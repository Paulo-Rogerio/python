""" 
Lista e um array, vetores 
- dinamicos
- podemos adicionar QUALQUER tipo de dados

Listas são representados por []
type([])

# Cria uma lista [0, 1, 2, 3 ,4]
list = list(range(5))


# Se tenho 2 valores e quero descartar, desprezar um.
# for _, i in enumerate(nome):
#     print(i)

"""

var = list(range(5))
if 4 in var:
    print("achei")

var = list('Paulo')
print(var.count('P'))

var = list(range(5))
print(var)
var.append(5)
print(var)

# uma lista dentro de outra lista

var = []
var1 = list(range(5))
var2 = list(range(5))
var.append(var1)
var.append(var2)
print(var)

# Informando a posicao do index
# Inserindo na posicao 1 o valor 99
var = []
var.append(1)
var.append(2)
print(var)
var.insert(1, 99)
print(var)

# Somando Listas
# Somando +
var = []
var1 = list(range(5))
var.append(5)
var.append(6)
print(var1 + var)

# Usando Extend
var = []
var1 = list(range(5))
var.append(5)
var.append(6)
var1.extend(var)
print(var1)

# Imprimindo reverso
var = list('Paulo')
var.reverse()
print(var)

# Imprimindo reverso - Usando slice
var = list('Paulo')
print(var[::-1])


var = list('Paulo')
var1 = var.copy()
print(var1)

# Contando elementos
print(len(var1))

# Removendo item da lista
# Ao remover ele mostra o elemento removido , removeu o ultimo elemento
# Index inicindo por 0

print(var1.pop())
print(var1)

print(var1.pop(3))
print(var1)

# Limpar a lista
print(var1.clear())

texto = 'Paulo Rogerio Gomes e Silva:'
print(texto)

# Cria a lista , split por padrao separa os elementos da lista usando espaço
var = texto.split()
print(var)

# Cria a lista , split separa os elementos da lista usando a string :
var = texto.split(':')
print(var)

# Converter lista em string
texto = ['Curso', 'Python']
print(texto)

# Coloca um espaco entre cada elemento
texto_string = ' '.join(texto)
print(texto_string)

soma = "bacate "
for i in texto:
    soma = f'{soma + i} '
print(soma)

cores = ['verde', 'amarelo']
print(cores[0])

# Imprime o ultimo elemento
print(cores[-1])

# Enumerate

print("=========== Enumerate ============")
for i, cor in enumerate(cores):
    print(i, cor)
    
# Em qual indice esta o valor 3

num = [0, 1, 2, 3, 3]
print(num.index(3))

# Qual index contem o numero 3, comece sua busca a partir do index 1
print(num.index(3, 1))

# Buscando o numero 3 dentro de um range de index ( 1 e 4 )
print(num.index(3, 1, 4))

# Comecando a impresao a partir do primeiro elemento
print(num[1:])

# Ate index 2
print(num[:2])

# Pego todos os elementos
print(num[::])

# Comeca pelo 1, vai ate o final de 2 em 2
print(num[1::2])
print(num[::2])

print("---------------------")
print(sum(num))
print(max(num))
print(min(num))
print(len(num))

# Convertento para tupla
print("---------------------")
print(tuple(num))

# Copiando os dados de uma lista para outra
# Nao interfere na original

print("---------------------")
nova = num.copy()
nova.append(5)
print(nova)

# Shallow Copy , acredito que deve fazer referencia ao mesmo objeto  ( num e nova2 )
nova2 = num
nova2.append(5)
print(nova2)
print(num)