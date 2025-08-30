# ex015 - Aluguel de Carros
# Solicita o número de dias e a quantidade de km rodados
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('\nAluguel de Carros')
dia = int(input('\nQuantos dias alugados? '))
km = float(input('Quantos km rodados? '))
v = (dia * 60) + (km * 0.15)
print(f'O total a pagar é de R$ {v:.2f}\n')
