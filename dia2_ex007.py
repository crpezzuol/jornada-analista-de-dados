# ex007 - Aumentos múltiplos

'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input("Digite o salário do funcionário: R$ \033[1;32m"))
print("\033[m", end='')
if salario > 1250:
    aumento = salario * 0.10  # aumento de 10%
else:
    aumento = salario * 0.15  # aumento de 15%
novo_salario = salario + aumento
print(f"Novo salário com aumento: R$ {novo_salario:.2f}")
