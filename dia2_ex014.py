# ex014 - Classificando Atletas

'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER
'''

# importando a biblioteca date para trabalhar com datas
from datetime import date

# importando a biblioteca os para limpar a tela do terminal
import os  

# limpando a tela do terminal
os.system('cls' if os.name == 'nt' else 'clear')

# imprimindo o cabeçalho do programa
print('\033[1;34m<>\033[m' * 30)
print('\n')

# lendo o ano de nascimento do atleta
ano_nasc = int(input('Ano de Nascimento: \033[1;32m'))
print('\033[m')

# calculando a idade do atleta
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f'O atleta tem {idade} anos.')

# classificando o atleta de acordo com a idade
if idade < 10:
    print('Classificação: \033[1;34mMIRIM\033[m')
elif idade < 15:
    print('Classificação: \033[1;34mINFANTIL\033[m')
elif idade < 20:
    print('Classificação: \033[1;34mJUNIOR\033[m')
elif idade < 26:
    print('Classificação: \033[1;34mSÊNIOR\033[m')
else:
    print('Classificação: \033[1;34mMASTER\033[m')
print('\n')
print('\033[1;34m<>\033[m' * 30)
print('\n')

# fim do programa
