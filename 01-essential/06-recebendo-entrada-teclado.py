from datetime import datetime

nome = input('Informe seu nome: ')
sobrenome = input('Informe seu sobrenome: ')
idade = int(input('Informe sua idade: '))
year = datetime.now().year

print("-------------------")

print(f'Olá !! Meu nome é {nome} {sobrenome} e tenho {idade} anos.')

print("-------------------")

print(f'{nome} {sobrenome}, vc nasceu em {year - idade}.')