"""
Operadores Lógicos: and , or, not , is

Operadores Unários: not

Operadores Binários: and, or, is
"""

ativo = True
logado = True

# Ambos variáveis devem ser True 
if ativo and logado:
    print('bem vindo usuário!!')
else:
    print('vc deve ativar sua conta !!')    

# Pelo menos 1 deve retornar True
if ativo or logado:
    print('bem vindo usuário!!')
else:
    print('vc deve ativar sua conta !!')    


if ativo is True and logado is True:
    print('bem vindo usuário!!')
else:
    print('vc deve ativar sua conta !!')    


a = [1, 2, 3]
b = [1, 2, 3]

# Is => compara se são o mesmo objeto na memória
print(a is b)
print("id de a:", id(a))
print("id de b:", id(b))

print(a == b)

flag = None

if flag is None:
    print("É exatamente Null")