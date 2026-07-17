# Usando para gerar sequencias de forma especificadas.
# range (1, 10)
# ultimo valor nao inclusivo.
# Se nao especificar o inicio, sempre comecara com 0

# for i in range(11):
#     print(i)

# Informando o passo
# Aqui e 2 em 2 comecando pelo 1
# for i in range(1, 11, 2):
#     print(i)
    
# Imorimindo forma inversa
# Valor de inicio + Valor de parada, ( -1 ) traz invertido a ordem
# for i in range(10, 0, -1):
#     print(i)
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

# Criar uma lista a partir de um range
lista = list(range(0,10))
print(lista)