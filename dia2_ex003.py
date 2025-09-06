'''
ex003 - Par ou Ímpar?
Peça para o usuário digitar um número e diga se ele é par ou ímpar
'''
num = int(input("Digite um número: \033[1;32m"))
print('\033[m')
if num % 2 == 0:
    print('O número digitado é par!')
else:
    print('O número digitado é ímpar!')
print('\n')
