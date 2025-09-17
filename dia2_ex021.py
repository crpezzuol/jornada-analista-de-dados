# ex021 - Soma ímpares múltiplos de três

'''
Crie um programa que mostre na tela a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

# importando a biblioteca os para limpar a tela
import os

# Limpando a tela (funciona tanto no Windows quanto no Linux/Mac)
os.system('cls' if os.name == 'nt' else 'clear')

# Declaração e inicialização de variáveis
cont = 0  # cont = contador de números solicitados
soma = 0  # soma = soma dos números solicitados

# imprimindo a soma dos números ímpares múltiplos de 3 no intervalo de 1 a 500
print('\n')
print('\033[1;32m=' * 10,'\033[1;36mSoma dos números ímpares múltiplos de 3 no intervalo de 1 a 500','\033[1;32m=\033[m' * 10)
print('\n')
for c in range(1, 501, 2):  # Percorre os números de 1 a 500, pulando de 2 em 2 (ou seja, só os ímpares)
    if c % 3 == 0:
        soma += c  # Soma os números ímpares múltiplos de 3
        cont += 1

# imprimindo o resultado
print('\033[1;32m=' * 16, f'\033[1;36mA soma de todos os {cont} valores solicitados é: {soma}.', '\033[1;32m=' * 16)
print('\033[m \n')
# Fim do programa
