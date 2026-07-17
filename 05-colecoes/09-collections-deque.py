"""
Deque e uma lista de alta performance
"""

from collections import deque

# Criou uma list a partir do nome passado ( Paulo )
deq = deque('Paulo')
print("------------")
print(deq)

# Adicinando Elementos no final ( Comportamento comum )
deq.append('R')
print("------------")
print(deq)

# Adicinona Elemento no inicio
deq.appendleft('C')
print("------------")
print(deq)

# Remove => Segue os mesmo padroes da Lista
# Removeu o R ( Ultimo elemento ) e retorna o elemento removido
deq.pop()
print("------------")
print(deq)

# Removeu  e retorna o primeiro elemento
deq.popleft()
print("------------")
print(deq)







