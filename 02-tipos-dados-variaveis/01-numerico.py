"""
Tipo Numérico
"""

# Divisao
print(5/2)

# Divisao ( modo pythonico , so imprime o inteiro)
print(5//2)

print(int(5/2))

# Modulo ( resto da divisao )
# 0 => par
# 1 => impar
print(5 % 2)

# Potencia
print(3 ** 3)

# Forma de declarar numero grandes ( _ ) e apenas o separador para humanos visuazliarem
# Resultado e : 1000000
print(1_000_000)

print("----------------")

# Incremento e Decremento
num = 10
print(num + 1)

num = 10
num += 1
print(num)

num = 10
num *= 2
print(num)

# Ambos tem o mesmo resultado
# recebo num e divido por 2 e armazeno na variavel num
num = num / 2
print(num)

num = 10
num *= 2

num /= 2
print(num)

print(type(num))

num = 10
print(num)
print(type(num))


print("-----------------")

# Listando funcao builtins
print("")
print(dir(num))

print("")
print("-----------------")
print("")

# Usando funcao builtins
print(num.__add__(8))