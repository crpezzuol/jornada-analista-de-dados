# ex012 - Calculando Descontos
prod = float(input('\nQual o preço da produto? R$ '))
print(f'\nO produto que custava R$ {prod:.2f}, na promoção com 5% de desconto, vai custar R$ {prod - (prod * 5 / 100):.2f}.\n')
