"""
Modulo collectioin counter

Collections => High Performance Container Datetypes

Counter => Reccebe um interavel como parametro e cria um objeto do tipo Collections Counter que e parecido com um dicionario,
contendo como chave o elemento da lista passada como parametro e como valor a quantidade de ocorrências desse elemento.
"""

from collections import Counter

lista = [1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5]

ret = Counter(lista)

# Esse e o tipo dele: <class 'collections.Counter'>
print(type(ret))

# Para elemento 1 encontrei 4 ocorrencias
# Para elemento 3 encontrei 1 ocorrencia
#
# Counter({1: 4, 5: 3, 2: 2, 3: 1, 4: 1})
print(ret)

# Counter({'P': 1, 'a': 1, 'u': 1, 'l': 1, 'o': 1})
# Para elemento P encontrei 1 ocorrencia
# Para elemento a encontrei 1 ocorrencia
#
print("--------------")
print(Counter('Paulo'))



print("--------------")
text="""
A Batalha de Três Lagoas foi uma ofensiva de revolucionários tenentistas contra as forças do governo do Brasil 
em 18 de agosto de 1924, estendendo a Revolta Paulista para o sul de Mato Grosso. 
Liderados por Juarez Távora, os revoltosos vindos de São Paulo sofreram baixas pesadas ao atacar o destacamento 
legalista do coronel Malan d'Angrogne, na localidade de Campo Japonês, ao sul de Três Lagoas. 
Esta derrota frustrou a ambição dos revoltosos de se fixar em Mato Grosso, obrigando-os a empreender a Campanha do Paraná.
"""

# Cria um array ( Lista ), com  cada palavra.
# Counter({'de': 9, 'do': 4, 'a': 4, 'Três':...........})
# Para palavra de encontrei 9 ocorrencia
# Para elemento do encontrei 4 ocorrencia
#
palavra = text.split()
ret = Counter(palavra)
print(ret) 

# 5 palavras que mais se repetem nesse texto. 5 palavras com mais ocorrencia no texto.
print("--------------")
print(ret.most_common(5))



