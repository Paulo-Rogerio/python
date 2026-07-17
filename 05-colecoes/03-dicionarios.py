"""
Em algumas linguagens os dicionarios são conhecidos como  mapas.

Sao coleções do tipo chave / valor

Dicionarios sao representados por { chave:valor }

Dicionarios não são indexados, nos dicioanarios usamos a chave para chegar no dado

Se tentar buscar um dado por uma chave inexistente ex: paises['py'], recebera um error KeyError

OBS.: NÃO PODEMOS TER CHAVES REPETIDAS

"""

print(type({}))

paises = {'br':'Brasil', 'eua':'Estados Unidos'}
print(type(paises))
print(paises)
print(paises['br'])

# Forma menos comum
print('---------------')
paises = dict(br='Brasil', eua='Estados Unidos')
print(paises)

# Forma recomendada ( Usando get )
# O get mesmo que a chave nao exista ele, retorna None ( vazio ), mas nao da Error.
# Mais simples de trabalhar principalmente com condicional

print(paises.get('br'))
print(paises.get('py'))

# Posso definir um valor padrao caso nao encontre
print(paises.get('br', 'Não Encontrado'))
print(paises.get('py', 'Não Encontrado'))

# Checa se determiinada chave existe no dicionario
print('---------------')
print('br' in paises)


print('---------------')
# (99.999, 99.001) => Isso é uma tupla
# E muito usual criar uma chave de um dicionario usando tuplas, pois elas são imutáveis
#  
localidades = {
    (99.999, 99.001): 'Escritorio Tokio',
    (88.888, 88.002): 'Escritorio Brasil'
}
print(type(localidades))
print(localidades)
print(localidades[(99.999, 99.001)])
print(localidades.get((10.0, 20.0), "Localidade não encontrada"))

# Adicioando Elemento a um dicionario ( mais comum )
print('---------------')
receita = { 'jan':'100', 'fev':'200', 'mar':'300' }
print(receita)
receita['abr'] = '400'
print(receita)

# Outra forma de adicionar elemento
new = {'mai':'500'}
receita.update(new)
print(receita)

# Posso usar esse formato para atulizar um elemento
new = {'mai':'600'}
receita.update(new)
print(receita)

# Remover um elemento
# Precisamos sempre informar a chave
# Retorna o valor retonado ( E preciso amarzenar isso em variavel ex: removi = receita.pop('mai') )
# + comum
receita.pop('mai')
print(receita)

# Delete e outra forma de remover um elemento
# Se a chave não existir retorna um KeyErro 
del receita['abr']
print(receita)

#=====================
# Simulando uma E-Commerce
# Produto, Qtd, Preco
print('---------------')
carrinho = []
produto1 = ['celular', 1, 1000.00]
produto2 = ['notbook', 1, 2000.00]
carrinho.append(produto1)
carrinho.append(produto2)

# Quem e quem aqui? Eu seu que o index 0 representa celular , e index 1 representa notebook. 
# Mas Preciso dar um rotulo para essa lista
print(type(carrinho))
print(carrinho)

# Usando Lista
carrinho = ()
print('---------------')
produto1 = ('celular', 1, 1000.00)
produto2 = ('notbook', 1, 2000.00)
carrinho = ( produto1, produto2 )
print(type(carrinho))
print(carrinho)

# Usando Dicionario
print('---------------')
carrinho = {}
compra = {"produto1": ("celular", 1, 1000.00)}
carrinho.update(compra)
compra = {"produto2": ("notebook", 1, 2000.00)}
carrinho.update(compra)
print(carrinho)

# Outra forma Usando Dicionario
# Defini quem e quem aqui....
# + usual
print('---------------')
carrinho = []
produto1 = { 'nome': 'celular', 'qtd': 1, 'valor': 1000.00 }
produto2 = { 'nome': 'notebook', 'qtd': 1, 'valor': 2000.00 } 
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)


# Limpar dicionario
print('---------------')
a = {'a':'a', 'b':'b'}
b = a.copy()
print(a)
a.clear()
print(a)

# Add um novo elemento em ( b )
b['c'] = 'c'
print(b)

# Shallow Copy ( Aqui acho que ele muda o object Id interno do python)
# Ambos foram modificados ( a e b )
print('---------------')
a = {'a':'a', 'b':'b'}
b = a
b['c'] = 'c'
print(a)
print(b)

# Uma forma nao usual de criar dicioanrio
print('---------------')
x = {}.fromkeys('a', 'a')
print(x)

# Todos os elementos dentro do [] vira uma chave e desconhecido e valor para todos eles
user = {}.fromkeys(['nome', 'pontos', 'email'], 'desconhecido')
print(user)

# Para cada letra do meu nome vira um chave com valor default letra
user = {}.fromkeys('paulo' 'letra')
print(user)

# Aqui uso o range para gerar numeros ate 10. Cada numero e a chave e o valore e num. 
user = {}.fromkeys(range(1, 11), 'num')
print(user)

# Iterando
print('---------------')
for i in user:
    print(i)

print('---------------')
for i in user:
    print(user[i])
    
print('---------------')
for i in user:
    print(f'{i} - {user[i]}')

# i representa o index
# j representa o value
# j e o chave desse dicionario
# user[j] e valor dessa dicionario    
print('---------------')
for i,j in enumerate(user):
    print(i,j,user[j],)

# Modo pythonico de usar
# Acessando as chaves
print('---------------')
print(user.keys())

for i in user.keys():
    print(i)

# Acessando os dicionario de valores
print('---------------')
print(user.values())

for i in user.values():
    print(i)
    
print('---------------')
print(sum(user.keys()))    