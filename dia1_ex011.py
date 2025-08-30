# ex011 - Pintando Parede
larg = float(input("\nDigite a largura da parede: "))
altu = float(input("Digite a altura da parede: "))
area = larg * altu
# Sabendo que cada litro de tinta pinta uma área de 2m²
litros = area / 2
print(f'\nSua parede tem a dimensão de {larg} X {altu} e sua área é de {area}m².')
print(f'Para pintar essa parede. você precisará de {litros}L de tinta.\n')
