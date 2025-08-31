# ex017 - Catetos e Hipotenusa
oposto = float(input('\nDigite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = (oposto**2 + adjacente**2)**0.5
print(f'\nA hipotenusa vai medir: {hipotenusa:.2f}\n')
# Obs: Também poderia ser usado a função hypot() da biblioteca math.
# Exemplo:
from math import hypot
hipotenusa = hypot(oposto, adjacente)
print(f'A hipotenusa vai medir: {hipotenusa:.2f}\n')
# Obs: Também poderia ser usado a função pow() para calcular a hipotenusa.
# Exemplo:
hipotenusa = pow(oposto**2 + adjacente**2, 1/2)
print(f'A hipotenusa vai medir: {hipotenusa:.2f}\n')
# Obs: Também poderia ser usado a função sqrt() da biblioteca math.
# Exemplo:
from math import sqrt
hipotenusa = sqrt(oposto**2 + adjacente**2)
print(f'A hipotenusa vai medir: {hipotenusa:.2f}\n')
