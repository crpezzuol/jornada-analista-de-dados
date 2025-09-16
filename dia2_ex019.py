# ex019 - Contagem regressiva
'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

# Importando a biblioteca time para usar a função sleep
from time import sleep

# importando a biblioteca os para limpar a tela
import os

# Limpando a tela (funciona tanto no Windows quanto no Linux/Mac)
os.system('cls' if os.name == 'nt' else 'clear')

# iniciando a contagem regressiva
print('\n' * 3)
print(' ' * 14, '\033[1;34mContagem regressiva para o \033[3;36mAno Novo!\033[m')
print('\n')
# Contagem regressiva de 10 até 0
for contagem in range(10, -1, -1):
    print('\033[5;32m ' * 31, contagem)  # Mostra o número atual da contagem
    sleep(1) # Pausa de 1 segundo

 # Mensagem final após a contagem   
print('\n')
print(' ' * 20, '\033[1;33mBUUMM!!! \033[1;32mPOW!!! \033[1;31mBANG!!!')
print('\033[m')
print(' ' * 24, '\033[4;36mFeliz Ano Novo!')
print('\n' * 3)
print('\033[m')

# Fim do programa
