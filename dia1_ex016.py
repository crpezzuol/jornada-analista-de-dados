# ex016 - Quebrando um número
num = float(input("\nDigite um valor: "))
print(f"O valor digitado foi {num:.3f} e a sua porção inteira é {int(num)}.\n")
# Obs: Também poderia ser usado a função math.trunc() para retirar a parte decimal.
# Exemplo:
from math import trunc
print(f"O valor digitado foi {num:.3f} e a sua porção inteira é {trunc(num)}.\n")
