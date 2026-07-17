"""
Tuplas são representadas por ()

Tuplas sao imultáveis , ao se criar uma tupla , ela não muda. Toda operação em uma tupla , gera uma nova tupla.

Lista sao multáveis...

O que define se e uma tupla e o uso da ,

Por serem imutaveis nao consigo apendar ( adicionar ou remover )

Ex de uso 

meses =('Janeiro', 'Fevereiro' ....)

E mais seguro pois e imutavel
E mais rapido

"""
var = ()
print(type(var))

# Ex com Lista 

var = [0, 5, 4, 6]
print(var)

var.sort()
print(var)


# Ex com Tuplas 
print("-----------------")
var = (0, 5, 4, 6)
print(var)
print(type(var))

# Isso tambem e uma tupla. Não e muito usual
print("-----------------")
var = 1, 2, 3, 4
print(var)
print(type(var))

# Isso nao e uma tupla , e sim um inteiro

print("-----------------")
var = (1)
print(var)
print(type(var))


# Isso é uma tupla

print("-----------------")
var = (1,)
print(var)
print(type(var))


# gerando Tupla dinamicamente
print("-----------------")
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento tupla
# Tenho declarado 2 valores, sou obrigado a definir 2 variaveis
print("-----------------")
tupla = ('Paulo Rogerio', 'Devops')
pessoa, cultura = tupla
print(pessoa)
print(cultura)
print(type(pessoa))
print(type(cultura))


print("-----------------")
tupla = (1, 2, 3)
print(sum(tupla))
print(len(tupla))
print(min(tupla))

# Concatenar Tupla
print("-----------------")
tupla1 = ( 1, 2, 3 )
tupla2 = ( 4, 5, 6 )
concat = tupla1 + tupla2
print(tupla1)
print(tupla2)
print(concat)

# Não posso alterar, mas posso sobrescrever o valor dela.
tupla1 = tupla1 + tupla2
print(tupla1)

# Checa se existe valor
print("-----------------")
print(2 in tupla1)

# Iterando
print("-----------------")
for i, j in enumerate(tupla1):
    print(i, j)

# Converter string em tupla
print("-----------------")
nome = tuple('Paulo')
print(nome)
print(nome.count('P'))


