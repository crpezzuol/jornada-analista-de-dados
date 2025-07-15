# dia1_logica.py
# Desafios do Dia 1 — Lógica de Programação com Python 🧠🔥

# 1️⃣ Número par ou ímpar
print("Desafio 1 — Número par ou ímpar")
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("É par!")
else:
    print("É ímpar!")

print("-" * 40)

# 2️⃣ Maior entre 3 números
print("Desafio 2 — Maior entre três números")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a >= b and a >= c:
    print(f"O maior número é: {a}")
elif b >= a and b >= c:
    print(f"O maior número é: {b}")
else:
    print(f"O maior número é: {c}")

print("-" * 40)

# 3️⃣ Calculadora simples
print("Desafio 3 — Calculadora Simples")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == "+":
    print("Resultado:", num1 + num2)
elif operacao == "-":
    print("Resultado:", num1 - num2)
elif operacao == "*":
    print("Resultado:", num1 * num2)
elif operacao == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Erro: divisão por zero")
else:
    print("Operação inválida")

print("-" * 40)

# 4️⃣ Tabuada com laço
print("Desafio 4 — Tabuada")
numero_tabuada = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{numero_tabuada} x {i} = {numero_tabuada * i}")

print("-" * 40)

# 5️⃣ Verificar se número é primo
print("Desafio 5 — Verificar número primo")
num = int(input("Digite um número: "))
eh_primo = True

if num <= 1:
    eh_primo = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            eh_primo = False
            break

if eh_primo:
    print(f"{num} é primo!")
else:
    print(f"{num} não é primo.")

print("-" * 40)