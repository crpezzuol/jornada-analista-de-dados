'''
ex004 - Custo da Viagem
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
'''

distancia = float(input("Qual é a distância da sua viagem? \033[1;32m"))
print('\033[m')
print(f'Você está prestes a começar uma viagem de {distancia} km.')

'''
print('Verificando o preço da passagem...')
if distancia <= 200:
    print(f'E o preço da sua passagem será de R$ {distancia * 0.50:.2f}')
else:
    print(f'E o preço de sua passagem será de R$ {distancia * 0.45:.2f}')
'''

# Usando o operador ternário para simplificar a lógica

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E o preço da sua passagem será de R$ {preco:.2f}')
print('\n')
