"""
Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""

a = 1
b = 2

if a > b:
    print(f'O maior e a => {a}')
else:
    print(f'O maior e b => {b}')
    
"""
Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido
"""

num = 9
if num < 0:
    print('Numero negativo')
else: 
    print(f'Raiz quadrada de {num} e : {round(num ** 0.5)}')       

"""
Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar
"""

num = 2
ret = num % 2

if ret == 0:
    print('Num par')
else:
    print('Num impar')