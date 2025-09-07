# ex006 - Maior e menor valores

'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

# Resolução Guanabara

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite um terceiro número: "))

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c
if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c
print(f"\nO menor número é: {menor}")
print(f"O maior número é: {maior}")

# Outra forma de fazer:

'''
maior = max(a, b, c)
menor = min(a, b, c)
'''
