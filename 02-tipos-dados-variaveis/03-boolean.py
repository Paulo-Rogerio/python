"""
Tipo Boolean

True  => Verdadeiro
False => False

Operaçoes Binarias ( Or )
True or True => True
True or False => True
False or True => True
False or False => False

Operaçoes Binarias ( And )
True and True => True
True and False => False
False and True => False
False and False => False

"""

status = True
print(type(status))

print('==================')
print(f'Status: {status}')

print('==================')
print(f'Status: {not status}')

print('==================')
a = True
b = False

print(f'Status Condicao (or) : {a or b}')

print('==================')
a = True
b = False

print(f'Status Condicao  (or) : {a and b}')
