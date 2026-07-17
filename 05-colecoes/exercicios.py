"""
1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores lidos.
"""

tupla = ('abacate', 'laranja', 1, 3, 'pequi', 4, 'goiaba', 2, 4.5, 5, 6)
lista = []
for i in tupla:
    if type(i) == int:
        lista.append(i)
lista.sort()
print(f'Os valores armazenados foram: {lista}')    
print("=======================")

"""
2. Faça um programa que possua uma lista denominada A que armazena 6 numeros inteiros. O programa deve executar os seguintes passos:
a) Atribua os seguintes valores a essas lista: 1, 0, 5, -2, -5, 7
b) Armazene em um variavel inteira a soma entre os valores das posições A[0], A[1], A[5] da lista e mostre na tela a soma.
c) Modifique a lista na posição 5, atribuindo a essa posição o valor 100.
d) Mostre na tela cada valor da lista , um em cada linha.
"""
# 
# Outra forma de declarar
# A: list[int] = [1, 0, 5, -2, -5, 7]

A = [1, 0, 5, -2, -5, 7]
soma = 0
for i, num in enumerate(A):
    if i in (0, 1, 5):
        if i == 5:
            num = 100
            soma += num
            print(f'Index: {i} - Value: {num}')
        else:
            soma += num
            print(f'Index: {i} - Value: {num}')
        
print(f'Soma: {soma}')
print("=======================")

"""
3. Faça um programa que leia 10 valores, armazene em uma lista e apresente quantos valores pares ele possui.
"""
lista = list(range(0,11))
for i in lista:
    if (i % 2) == 0:
        print(i)
 

    
