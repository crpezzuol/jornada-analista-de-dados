# ex017 - Gerenciador de Pagamentos
'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros
'''
# início do programa

# importando a biblioteca os para limpar a tela
import os

# Limpando a tela
os.system('cls' if os.name == 'nt' else 'clear')

# cabeçalho do programa
print('\033[1;32m<>\033[1;33m<>' * 10,'\033[1;36mLOJAS  PEZZUOL','\033[1;32m<>\033[1;33m<>' * 10)
print('\n\033[m')

# entrada de dados
compra = float(input('Preço das compras: R$ \033[1;32m'))
print('\n\033[m')

# opções de pagamento
print('''FORMAS DE PAGAMENTO \033[1;34m>\033[m\n
    \033[1;34m[\033[m \033[1;33m1\033[m \033[1;34m]\033[m à vista dinheiro/cheque
    \033[1;34m[\033[m \033[1;33m2\033[m \033[1;34m]\033[m à vista cartão
    \033[1;34m[\033[m \033[1;33m3\033[m \033[1;34m]\033[m 2x no cartão 
    \033[1;34m[\033[m \033[1;33m4\033[m \033[1;34m]\033[m 3x ou mais no cartão
''')

# escolha do pagamento
pagamento = int(input('Qual a opção? \033[1;32m'))
print('\n\033[m')

# cálculo do valor final conforme a forma de pagamento
if pagamento == 1:
    print(f'Sua compra de R$ {compra:.2f} com desconto de \033[1;32m" 10% "\033[m vai custar R$ \033[1;32m{compra * 0.9:.2f}\033[m no final.')
elif pagamento == 2:
    print(f'Sua compra de R$ {compra:.2f} com desconto de \033[1;32m" 5% "\033[m vai custar R$ \033[1;32m{compra * 0.95:.2f}\033[m no final.')
elif pagamento == 3:
    print(f'Sua compra de R$ {compra:.2f} \033[1;31m" SEM DESCONTO"\033[m vai custar R$ \033[1;32m{compra:.2f}\033[m.') 
elif pagamento == 4:
    parcelas = int(input('Em quantas parcelas deseja pagar? \033[1;32m'))
    parc_juros = (compra * 1.2) / parcelas
    print(f'\n\033[mSua compra será parcelada em \033[1;34m{parcelas}X\033[m de R$ \033[1;31m{parc_juros:.2f} COM JUROS DE " 20% "\033[m.')
    print(f'Sua compra de R$ \033[1;32m{compra:.2f}\033[m vai custar R$ \033[1;31m{parcelas * parc_juros:.2f}\033[m no final.\n')
else:     
    print('\033[1;31mOpção de Pagamento INVÁLIDA! Tente Novamente!\033[m')
print('\n')
print('\033[1;32m<>\033[1;33m<>' * 24)
print('\n\033[m')

# fim do programa
