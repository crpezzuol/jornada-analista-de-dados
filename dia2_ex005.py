# ex005 - Ano Bissexto

'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

# Solução do Guanabara

'''
from datetime import date

try:
    ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: \033[1;32m').strip())
except ValueError:
    print("\033[1;31mDigite apenas números inteiros!\033[m")
    exit()
print('\033[m')
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
print('\n')
'''

import calendar 
# Obs: A biblioteca calendar já possui uma função que verifica se o ano é bissexto ou não.

from datetime import date

try:
    ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: \033[1;32m').strip())
except ValueError:
    print("\033[1;31mDigite apenas números inteiros!\033[m")
    exit()
print('\033[m')

if ano == 0:
    ano = date.today().year

if calendar.isleap(ano):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
print('\n')
