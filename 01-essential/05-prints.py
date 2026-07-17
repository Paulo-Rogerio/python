"""
dir(__builtins__)

Formas de imprimir

Os dados vindo do input vem com o tipo string, quero converte-lo para i 
"""


nome = input('Informe seu nome: ')
sobrenome = input('Informe seu sobrenome: ')
idade = input('Informe sua idade: ')


# Concatenando
print('Olá !! Meu nome é ' + nome + ' ' + sobrenome + ' e tenho ' + str(idade) + ' anos.') 

print("-------------------")

# Forma antiga de imprimir
print('Olá !! Meu nome é %s %s e tenho %s anos.' % (nome, sobrenome, int(idade))) 

print("-------------------")

# Outra Forma de imprimir
print('Olá !! Meu nome é {0} {1} e tenho {2} anos.'.format(nome, sobrenome, int(idade)))

print("-------------------")

# Forma Atual de imprimir
print(f'Olá !! Meu nome é {nome} {sobrenome} e tenho {int(idade)} anos.')


# Variaveis podem ser definidas com aspas simples ou duplas.
nome = "Paulo"
sobrenome = 'Rogerio'
idade = 39

# Concatenando
print('Olá !! Meu nome é ' + nome + ' ' +
      sobrenome + ' e tenho ' + str(idade) + ' anos')
print("-------------------")

# string formatada
print('Olá !! Meu nome é {} {} e tenho {} anos'.format(nome, sobrenome, idade))
print("-------------------")

# Ordem das variáveis devem ser sequencias pois não está explicitado.
print('Olá !! Meu nome é {} {} e tenho {} anos'.format(idade, sobrenome, nome))
print("-------------------")

# Explicitando o nome das variáveis, assim ela não precisa ser sequencial.
print('Olá !! Meu nome é {n} {s} e tenho {i} anos'.format(
    i=idade, s=sobrenome, n=nome))