# ex018 - GAME: Pedra Papel e Tesoura

'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
# início do programa

# importando as bibliotecas os, randint e sleep
import os
from random import randint
from time import sleep

# Limpando a tela
os.system('cls' if os.name == 'nt' else 'clear')

# cabeçalho do programa
print('\033[1;32m<>\033[1;33m<>' * 10,'\033[1;36mJOKENPÔ - PEDRA, PAPEL E TESOURA','\033[1;32m<>\033[1;33m<>' * 10)
print('\n\033[m')

# opções do jogo 
opcoes = ['PEDRA', 'PAPEL', 'TESOURA'] 
print('''\033[1;34mSuas opções são:\033[m\n
    \033[1;34m[\033[m \033[1;33m0\033[m \033[1;34m]\033[m PEDRA
    \033[1;34m[\033[m \033[1;33m1\033[m \033[1;34m]\033[m PAPEL
    \033[1;34m[\033[m \033[1;33m2\033[m \033[1;34m]\033[m TESOURA
    \033[1;34m[\033[m \033[1;33m3\033[m \033[1;34m]\033[m SAI FORA
''')
# escolha do jogador
jogador = int(input('Qual a sua jogada? \033[1;32m'))
print('\033[m')
if jogador == 3:
    print('\033[1;31mVocê saiu do jogo!\033[m')
    print('\n')
    exit()
elif jogador < 0 or jogador > 3:
    print('\033[1;31mJOGADA INVÁLIDA! TENTE NOVAMENTE!\033[m')
    print('\n')
    exit()

# escolha do computador
computador = randint(0, 2)   

# contagem para o jogo
sleep(0.5)
print('\033[1;33mJO')
sleep(1)
print('\033[1;32mKEN')
sleep(1)
print('\033[1;34mPÔ!!!\033[m')
print('\n')

# mostrando as escolhas
print(f'Jogador jogou \033[1;32m{opcoes[jogador]}\033[m')
print(f'Computador jogou \033[1;31m{opcoes[computador]}\033[m')
print('\n')

# verificando o resultado
if jogador == computador:
    print('\033[1;32mEMPATOU!\033[m')   
elif jogador == 0 and computador == 1:
    print('O JOGADOR \033[1;31mPERDEU!\033[m')
elif jogador == 0 and computador == 2:
    print('O JOGADOR \033[1;32mGANHOU\033[m')
elif jogador == 1 and computador == 0:
    print('O JOGADOR \033[1;32mGANHOU\033[m')
elif jogador == 1 and computador == 2:
    print('O JOGADOR \033[1;31mPERDEU!\033[m')
elif jogador == 2 and computador == 0:
    print('O JOGADOR \033[1;31mPERDEU!\033[m')
elif jogador == 2 and computador == 1:
    print('O JOGADOR \033[1;32mGANHOU\033[m')
print('\n')
print('\033[1;32m<>\033[1;33m<>' * 28 + '\033[1;32m<>')
print('\n\033[m')

# fim do programa
