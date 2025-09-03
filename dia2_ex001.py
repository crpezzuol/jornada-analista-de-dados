# ex001 - Jogo da Adivinhação v.1.0
# Crie um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep 
computador = randint(0, 5) # computador sorteia um número entre 0 e 5
print('\033[1;33m-=-' * 21)
print('\033[1;33m| \033[1;34mVou pensar em um número entre 0 e 5...   Tente adivinhar... \033[1;33m|')
print('\033[1;33m-=-' * 21,'\n\033[m')
jogador = int(input('Em que número eu pensei? (0 a 5): ')) # jogador tenta adivinhar o número
print('\n\033[1;32mPROCESSANDO...\033[m\n')
sleep(2) # espera 2 segundos para mostrar o resultado
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!\n')
    print(f'Eu pensei no número {computador} e você acertou!\n')
else:
    print(f'\nGanhei! Eu pensei no número {computador} e não no {jogador}.\n')
