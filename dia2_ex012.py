# ex012 - Alistamento Militar

'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

# Importando a biblioteca date do módulo datetime
from datetime import date

# Importando a biblioteca os para limpar a tela
import os

# Limpando a tela
os.system('cls' if os.name == 'nt' else 'clear')    

# Iniciando o programa
print('\n')
ano_nasc = int(input("Digite seu ano de nascimento: \033[1;32m"))
print('\033[m')
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f"Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.")
if idade == 18:
    print(f"Você tem que se alistar \033[1;31mIMEDIATAMENTE!")
    print('\033[m')
elif idade < 18:
    print(f"Ainda faltam \033[1;31m{18 - idade}\033[m anos para você se alistar.")
    print(f"Seu alistamento será em \033[1;32m{ano_nasc + 18}\033[m.")
    print('\033[m')
else:
    print(f"Você já deveria ter se alistado há \033[1;31m{idade - 18}\033[m anos.")
    print(f"Seu alistamento foi em \033[1;32m{ano_nasc + 18}\033[m.")
    print('\033[m')
# Finalizando o programa
print('\n')
