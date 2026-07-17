"""
Tipo Fload

Tipo real, decimal

Casas decimais

Separador de casas decimas e o ( . )
Ex: 1.44

"""

# Gera uma Tupla, isso nao e um float
valor = 1,44
print(type(valor))

# Float
valor = 1.44
print(type(valor))

# Dupla atribuicao na mesma linha
# Int
valor1, valor2 = 1, 44
print(type(valor1))
print(type(valor2))


# Conversao float para inteiro , perde-se precisao
i = int(valor)
print(i)

print('==================')
print('Numeros complexos: Representados por Xj')

num = 5j
print(type(num))