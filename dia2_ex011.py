# ex011 - Comparando números

'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
O primeiro valor é maior;
O segundo valor é maior;
Não existe valor maior, os dois são iguais.
'''

# Importa o módulo os para limpar a tela

import os

# Limpa a tela (Windows/Linux/Mac)

os.system('cls' if os.name == 'nt' else 'clear')

# Início do exercício

print('\n')
print('\033[1;33m-=' * 20)
print('\033[1;33m---------- \033[1;31mComparando Números \033[1;33m----------')
print('\033[1;33m-=' * 20)
print('\033[m')

# Solicita ao usuário dois números inteiros

try:
    n1 = int( input("Digite o primeiro número: \033[32m"))
except ValueError:
    print('\033[31mEntrada inválida! Por favor, digite um número inteiro.\033[m')
    n1 = int( input("Digite o primeiro número: \033[32m"))
try:
    n2 = int( input("\033[mDigite o segundo número: \033[32m")) 
except ValueError:
    print('\033[31mEntrada inválida! Por favor, digite um número inteiro.\033[m')
    n2 = int( input("\033[mDigite o segundo número: \033[32m"))
print('\033[m')

# Compara os dois números e imprime o resultado

if n1 > n2:
    print("O primeiro número é maior.")
elif n2 > n1:
    print("O segundo número é maior.")
else:
    print("Os dois números são iguais.")

print('\n')

# Fim do exercício
