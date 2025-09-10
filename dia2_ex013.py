# ex013 - Aquele clássico da Média

'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO
'''

# Importando a biblioteca os para limpar a tela
import os

# Limpando a tela
os.system('cls' if os.name == 'nt' else 'clear')

# Iniciando o programa
print('\n')

# Solicitando as notas do aluno
n1 = float(input("Digite a \033[1;34mprimeira\033[m nota: \033[1;32m"))
n2 = float(input("\033[mDigite a \033[1;34msegunda\033[m nota: \033[1;32m"))
print('\033[m')

# Calculando a média do aluno
media = (n1 + n2) / 2

# Mostrando o resultado final
if media < 5.0:
    print(f"A média é igual a \033[1;31m{media:.2f}!\033[m E o Aluno está \033[1;31mREPROVADO!\033[m")
elif 5.0 <= media <= 6.9:
    print(f"A média é igual a \033[1;33m{media:.2f}!\033[m E o Aluno está de \033[1;33mRECUPERAÇÃO!\033[m")
else:
    print(f"A média é igual a \033[1;32m{media:.2f}!\033[m E o Aluno está \033[1;32mAPROVADO!\033[m")
print('\n')

# Fim do programa
