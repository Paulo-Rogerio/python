"""
1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
maiores que 0.
"""
num = []
count = 1
while True:
    if ( count % 3 ) == 0:
        num.append(count)
    if (len(num) == 5):
        break
    count += 1
print(num)
    

"""
2. Faça um programa que utilize o comando while para mostrar na tela uma contagem regressiva, iniciando
em 10 e terminando em 0. Mostre também uma mensagem “FIM!” após a contagem.
"""

num = ''
while True:
    for i in range(10, -1, -1):
        num = i
        print(i)
    if num == 0:
        break
print('FIm!')

"""
3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo
seu valor na tela, até que seu valor seja 100000 (cem mil).
"""
 
num = 0
while True:
    if num == 100000:
        break
    num += 1000
print(num)


for i in range(0, 1000001, 1000):
    print(i)
    
