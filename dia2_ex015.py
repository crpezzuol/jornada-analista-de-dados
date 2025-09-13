# ex015 - Analisando Triângulos v2.0

'''
Refaça o DESAFIO dia2_ex008.py dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes
'''
# importando a biblioteca os para limpar a tela do terminal
import os
# limpando a tela do terminal
os.system('cls' if os.name == 'nt' else 'clear')
# imprimindo o cabeçalho do programa
print('\033[1;34m<>\033[m' * 35)
print('\n')
# lendo o comprimento dos lados do triângulo
a = float(input('Primeiro segmento: \033[1;32m'))
b = float(input('\033[mSegundo segmento: \033[1;32m'))
c = float(input('\033[mTerceiro segmento: \033[1;32m'))
print('\n\033[m')
# verificando se os segmentos podem formar um triângulo
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima \033[1;32mPODEM FORMAR\033[m formar um TRIÂNGULO ', end = '')
    if a == b == c: # outra forma de fazer igualdade
        print('\033[1;32mEQUILÁTERO!\033[m\n')
    elif a != b != c != a: # outra forma de fazer diferenças
        print('\033[1;32mESCALENO!\033[m\n')
    else:
       print('\033[1;32mISÓSCELES!\033[m\n')
else:
    print('Os segmentos acima \033[1;31mNÃO PODEM\033[m formar um \033[1;31mTRIÂNGULO!\n')
print('\033[1;34m<>\033[m' * 35)
print('\n')
# fim do programa

