# Modelo simples com if/elif/else.

# ex010 - Conversor de Bases Numéricas

'''
Crie um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 - para binário
2 - para octal
3 - para hexadecimal
'''

# Importa o módulo os para usar comandos do sistema operacional

import os 

# Limpa a tela (Windows/Linux/Mac)

os.system('cls' if os.name == 'nt' else 'clear')
'''
os.system('cls') # Limpa a tela (Windows)
os.system('clear') # Limpa a tela (Linux/Mac) 
'''

# Início do exercício

print('\n')
print('\033[1;33m-=' * 20)
print('\033[1;33m----- \033[1;31mConversor de Bases Numéricas \033[1;33m-----')
print('\033[1;33m-=' * 20)
print('\033[m')

# Solicita ao usuário um número inteiro e a base para conversão

num = int(input("Digite um número inteiro: \033[32m"))
print('\033[m')
base = int(input('Escolha uma das bases para conversão: \n'
              '\n\033[1;32m1 - \033[mBinário'    
              '\n\033[1;32m2 - \033[mOctal'
              '\n\033[1;32m3 - \033[mHexadecimal\n'
              '\n\033[mSua opção: \033[1;32m'))
print('\033[m')

# Realiza a conversão e exibe o resultado

if base == 1:
    print(f'O número \033[32m{num}\033[m em binário é: \033[34m{bin(num)[2:]}\033[m')
elif base == 2:
    print(f'O número \033[32m{num}\033[m em octal é: \033[34m{oct(num)[2:]}\033[m')
elif base == 3:
    print(f'O número \033[32m{num}\033[m em hexadecimal é: \033[34m{hex(num)[2:]}\033[m')
else:
    print('\033[31mOpção inválida! Escolha uma base válida.\033[m')
print('\n')

# Fim do exercício


# Usando try/except para tratar entradas inválidas, tornando-o mais robusto para uso real e mais pythonico por prever entradas erradas.

''' 

# ex010 - Conversor de Bases Numéricas

# Importa o módulo os para usar comandos do sistema operacional
import os 

# Limpa a tela (Windows/Linux/Mac)
os.system('cls' if os.name == 'nt' else 'clear')

# Início do exercício
print('\n')
print('\033[1;33m-=' * 20)
print('\033[1;33m----- \033[1;31mConversor de Bases Numéricas \033[1;33m-----')
print('\033[1;33m-=' * 20)
print('\033[m')

# Solicita ao usuário um número inteiro e a base para conversão
try:
    num = int(input("Digite um número inteiro: \033[32m"))
    print('\033[m')
    base = int(input('Escolha uma das bases para conversão: \n'
                      '\n\033[1;32m1 - \033[mBinário'
                      '\n\033[1;32m2 - \033[mOctal'
                      '\n\033[1;32m3 - \033[mHexadecimal\n'
                      '\n\033[mSua opção: \033[1;32m'))
    print('\033[m')

    # Realiza a conversão e exibe o resultado
    if base == 1:
        print(f'O número \033[32m{num}\033[m em binário é: \033[34m{bin(num)[2:]}\033[m')
    elif base == 2:
        print(f'O número \033[32m{num}\033[m em octal é: \033[34m{oct(num)[2:]}\033[m')
    elif base == 3:
        print(f'O número \033[32m{num}\033[m em hexadecimal é: \033[34m{hex(num)[2:]}\033[m')
    else:
        print('\033[31mOpção inválida! Escolha uma base válida.\033[m')

except ValueError:
    print('\033[31mEntrada inválida! Por favor, digite um número inteiro.\033[m')

print('\n')

# Fim do exercício
'''

# Este código utiliza um dicionário para mapear as opções de conversão, tornando-o mais escalável e fácil de manter.

'''
# ex010 - Conversor de Bases Numéricas

"""
Crie um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 - para binário
2 - para octal
3 - para hexadecimal
"""

import os

# Limpa a tela (funciona no Windows, Linux e Mac)
os.system('cls' if os.name == 'nt' else 'clear')

print('\n')
print('\033[1;33m-=' * 20)
print('\033[1;33m----- \033[1;31mConversor de Bases Numéricas \033[1;33m-----')
print('\033[1;33m-=' * 20)
print('\033[m')

try:
    # Entrada do número
    num = int(input("Digite um número inteiro: \033[32m"))
    print('\033[m')

    # Menu de opções
    base = int(input(
        'Escolha uma das bases para conversão: \n'
        '\n\033[1;32m1 - \033[mBinário'
        '\n\033[1;32m2 - \033[mOctal'
        '\n\033[1;32m3 - \033[mHexadecimal\n'
        '\n\033[mSua opção: \033[1;32m'))
    print('\033[m')

    # Dicionário de opções
    conversoes = {
        1: ("binário", bin),
        2: ("octal", oct),
        3: ("hexadecimal", hex)
    }

    if base in conversoes:
        nome, funcao = conversoes[base]
        print(f'O número \033[32m{num}\033[m em {nome} é: \033[34m{funcao(num)[2:]}\033[m')
    else:
        print('\033[31mOpção inválida! Escolha uma base válida.\033[m')

except ValueError:
    print('\033[31mEntrada inválida! Por favor, digite um número inteiro.\033[m')

print('\n')

# Fim do exercício
'''
