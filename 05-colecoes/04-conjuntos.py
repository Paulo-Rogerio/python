"""
Conjuntos sao chamados de Set

De forma semalhante na matematica :
- Set ( conjuntos ) não possui valores duplicados
- Set ( conjuntos ) não possui valores ordenados
- Set ( conjuntos ) Os elementos não sao acessados via índice, ou seja, conjuntos não sao indexados 

Em que cenarios poderia ser aplicado?
- Quando precisamos armazenar elementos mas não nos importamos com a ordenação deles. Quando não precisamos nos preucupar com chave, valores e items duplicados.

Os conjuntos sao referenciados com {}

Como diferenciar mapas ( Mapas ) de conjuntos ( Set ) , visto que ambos são referenciados por {}
- Um dicionario ( mapa ) tem chave/valor
- Um conjunto tem apenas valor

"""

# O conjunto ignora valores repetidos, sem gerar erro
s = set({1, 2, 3, 4, 3, 4})
print("===============")
print(type(s))
print(s)

# Convertendo uma lista com itens repetidos para conjunto
print("===============")
lista = [0, 1, 2 , 3, 4, 4]
print(lista)
print(set(lista))

# Convertendo uma tupla com itens repetidos para conjunto
print("===============")
tupla = (0, 1, 2 , 3, 4, 4)
print(tupla)
print(set(tupla))

# Obs.: Nao e ordenado

dados = [99, 100, 0, 1, 2, 3, 4, 4, 5, 5]
lista = list(dados)
tupla = tuple(dados)
dicionario = {}.fromkeys(dados, 'numero')
conjunto = set(dados)

# Dicionario nao repete chaves
# Conjunto nao repete valores

print("===============")
print(f'Lista: {lista} com {len(lista)} elementos')
print(f'Tupla: {tupla} com {len(tupla)} elementos')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')


print("===============")
print('Podemos misturar dados')
dados = {1, 'dddd', 1.5 }
print(type(dados))
print(dados)

# Lista das cidades das pessoas que visitaram um derminado museu. 
print("===============")
cidades = ["Goiania", "Goiania", "São Paulo", "Rio de Janeiro", "Rio de Janeiro"]
print(len(cidades))

# Quantas cidades distintas ( deferente ) temos?
# Set remove duplicidade.
print(len(set(cidades)))
print(set(cidades))

# Conjunto são mutaveis
# Duplicidade não gera erro, mas não adiciona no connjuto 
print("===============")
dados = {0, 1, 2}
dados.add(3)
dados.add(3)
print(dados)

# Remover um elemento de um conjunto
# Esse "3" não e index, e o valor literal
# Conjunto não sao indexado
# Se valor não for encontrado, vai gerar error
dados.remove(3)
print(dados)

# Se o valor não e encontrado, não gera-se Error
dados.discard(3)
print(dados)


# Copiando um conjunto para outro.
# Deep Copy
# 2 Elementos ( 2 Objetos ) totalmente isolados um do outro
print("===============")
elemento_1 = {0, 1}
elemento_2 = elemento_1.copy()
elemento_2.add(3)
print(elemento_1)
print(elemento_2)

# Shallow Copy
# Aqui os 2 elementos serão modificados
# Compartilham o mesmo espaco de memoria
print("===============")
elemento_1 = {0, 1}
elemento_2 = elemento_1
elemento_2.add(3)
print(elemento_1)
print(elemento_2)

# Metodos matematicos conjunto
estudante_python = { 'Benicio', 'Alvaro', 'Paulo' }
estudante_golang = { 'Camilla', 'Paulo' }

# Gerar conjunto com nome de todos os estudantes
# Union
print("===============")
estudantes = estudante_python.union(estudante_golang)
print(estudantes)
# So muda a ordem
estudantes = estudante_golang.union(estudante_python)
print(estudantes)

# Gerar conjunto com nome de todos os estudantes
# Union usando |
print("===============")
estudantes2 = estudante_python | estudante_golang
print(estudantes2)
estudantes2 = estudante_golang | estudante_python
print(estudantes2)



# Gerar conjunto com nome de todos os estudantes
# Interseção
# Alunos que estudam python e golang
print("===============")
estudantes = estudante_python.intersection(estudante_golang)
print(estudantes)

# OUtra forma
estudantes = estudante_python & estudante_golang
print(estudantes)

# Diferenca
# Pega Somente quem faz curso python e somente quem faz curso golang
print("===============")
so_python = estudante_python.difference(estudante_golang)
so_golang = estudante_golang.difference(estudante_python)
print(f'So python: {so_python}')
print(f'So golang: {so_golang}')

