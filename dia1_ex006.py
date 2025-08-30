# ex006 - Dobro, Triplo, Raiz Quadrada
n = int(input('\nDigite um número: '))
print(f'\nO dobro de {n} vale {n*2}')
print(f'O triplo de {n} vale {n*3}')
print(f'A raiz quadrada de {n} vale {n**(1/2):.2f}\n')
# Usando a função pow
print(f'A raiz quadrada de {n} vale {pow( n,1/2):.2f}\n')
# Usando a função sqrt
from math import sqrt
print(f'A raiz quadrada de {n} vale {sqrt(n):.2f}\n')
