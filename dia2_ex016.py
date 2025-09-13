# ex016 - Índice de Massa Corporal

'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
IMC abaixo de:
18,5: Abaixo do Peso
IMC entre:
18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida
'''

# início do programa  

# importando a biblioteca os para limpar a tela
import os

# Limpando a tela
os.system('cls' if os.name == 'nt' else 'clear')
  
# cabeçalho do programa
print('\033[1;34m=' * 43)
print('=== \033[1;36mCálculo do Índice de Massa Corporal \033[1;34m===')
print('=' * 43)
print('\033[m')

# entrada de dados
peso = float(input('Digite seu peso (kg): \033[1;32m'))
altura = float(input('\033[mDigite sua altura (mts): \033[1;32m'))
print('\033[m')

# calculo do IMC
imc = peso / (altura ** 2)

# mostrando o resultado
print(f'Seu IMC é \033[1;34m{imc:.1f}')

# análise do IMC
if imc < 18.5:
    print('\033[1;31mCUIDADO! \033[mvocê está \033[1;31mABAIXO DO PESO!')
elif 18.5 <= imc <= 25:
    print('\033[1;32mPARABÉNS \033[mseu peso está \033[1;32mNORMAL!')
elif 25 > imc <= 30:
    print('\033[1;31mCUIDADO! \033[mvocê está com \033[1;31mSOBREPESO!')
elif 30 > imc <= 40:
    print('\033[1;31mCUIDADO! \033[mvocê está \033[1;31mOBESO!')
else:
    print('\033[1;31mCUIDADO! \033[mvocê está com \033[1;31mOBESIDADE MÓRBIDA!')
print('\n')
print('\033[1;34m=' * 43)
print('\033[m')

# fim do programa
