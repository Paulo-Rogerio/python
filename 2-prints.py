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