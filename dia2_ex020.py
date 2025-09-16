# ex020 - Contagem de pares
'''
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''

# Importando a biblioteca time para usar a função sleep
from time import sleep

# importando a biblioteca os para limpar a tela
import os

# Limpando a tela (funciona tanto no Windows quanto no Linux/Mac)
os.system('cls' if os.name == 'nt' else 'clear')

# imprimindo numeros pares de 0 a 50
print('Imprimindo números pares de 0 a 50.')
print('\n')
sleep(0.5)
for c in range(2, 51, 2):
    print(' ' * 16, c)
    sleep(0.3)  # Atraso de 0.1 segundos entre os números
print('\nFim da contagem de números pares de 0 a 50.')
print('\n' * 3)

# Fim do programa
