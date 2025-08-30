# ex007 - Média Aritmética
nota1 = float(input("\nDigite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
print(f"\nA média entre {nota1:.1f} e {nota2:.1f} é igual a {(nota1 + nota2) / 2:.2f}\n")
# Usando a função mean
from statistics import mean
print(f"A média entre {nota1:.1f} e {nota2:.1f} é igual a {mean([nota1, nota2]):.2f}\n")
