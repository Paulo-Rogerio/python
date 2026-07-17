"""
Condicionais: if / else / elif

"""

idade = 61

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem exatamente 18 anos')
else:
    if idade > 60:
        print('idoso')
    else:
        print('Maior de idade')