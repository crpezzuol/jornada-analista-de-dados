# ex024 - Primeiro e último nome de uma pessoa
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("\nDigite seu nome completo: "))
print('\nÉ um prazer te conhecer!\n')
print(f'Seu primeiro nome é {nome.split()[0]}.')
print(f'Seu último nome é {nome.split( )[-1]}.\n')  
