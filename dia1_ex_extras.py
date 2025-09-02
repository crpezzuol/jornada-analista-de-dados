# 📌 Exercícios Extras – Fixação Dia 1 🧠🔥

# 1️⃣ **Dobro, Triplo e Raiz Cúbica**
# Crie um algoritmo que peça um número inteiro e mostre o dobro, o triplo e a raiz cúbica (com duas casas decimais).
print("\n" + "📌" * 10 + " Exercícios Extras – Fixação Dia 1 🧠🔥 " + "📌" * 10 + "\n")
print("1️⃣  Dobro, Triplo e Raiz Cúbica:\n")
num = int(input("Digite um número inteiro: \033[1;32m "))
dobro = num * 2
triplo = num * 3
raiz_cubica = num ** (1/3)
print(f"\033[m\nO dobro de {num} é {dobro}")
print(f"O triplo de {num} é {triplo}")
print(f"A raiz cúbica de {num} é {raiz_cubica:.2f}\n")

# 2️⃣ **Conversor de Temperatura (Fahrenheit → Celsius/Kelvin)**
# Peça a temperatura em Fahrenheit e mostre a conversão em Celsius e Kelvin.
print("2️⃣  Conversor de Temperatura (Fahrenheit → Celsius/Kelvin:)\n")
fah = float(input("Digite a temperatura em Fahrenheit: \033[1;32m "))
celsius = (fah - 32) * 5/9
kelvin = celsius + 273.15
print(f"\033[m\nA temperatura de {fah}°F corresponde a {celsius:.2f}°C")
print(f"E a temperatura de {fah}°F corresponde a {kelvin:.2f}K\n")

# 3️⃣ **Calculadora de Viagem**
# Peça a distância de uma viagem (km) e a velocidade média do carro (km/h).
# Mostre quanto tempo levará para concluir a viagem.
print("3️⃣  Calculadora de Viagem:\n")
distancia = float(input("Digite a distância da viagem em km: \033[1;32m "))
velocidade = float(input("\033[mDigite a velocidade média do carro em km/h: \033[1;32m "))
tempo = distancia / velocidade  # Tempo em horas
print(f"\033[m\nA viagem de {distancia} km a uma velocidade média de {velocidade} km/h levará {tempo:.2f} horas.\n")

# 4️⃣ **Desconto Progressivo**
# Peça o valor de um produto e mostre o preço com:
# * 5% de desconto
# * 10% de desconto
# * 20% de desconto
print("4️⃣  Desconto Progressivo:\n")
preco = float(input("Digite o valor do produto: \033[1;32m R$ "))
desconto_5 = preco * 0.95
desconto_10 = preco * 0.90
desconto_20 = preco * 0.80
print(f"\033[m\nO preço do produto com 5% de desconto é R$ {desconto_5:.2f}")
print(f"O preço do produto com 10% de desconto é R$ {desconto_10:.2f}")
print(f"O preço do produto com 20% de desconto é R$ {desconto_20:.2f}\n")

# 5️⃣ **Conversor de Idade**
# Peça a idade de uma pessoa em anos e mostre:
# * Quantos meses ela viveu
# * Quantas semanas
# * Quantos dias (considerando 365 dias por ano)
print("5️⃣  Conversor de Idade:\n")
idade_anos = int(input("Digite a idade da pessoa em anos: \033[1;32m "))
idade_meses = idade_anos * 12
idade_semanas = idade_anos * 52
idade_dias = idade_anos * 365
print(f"\033[m\nA pessoa viveu {idade_meses} meses")
print(f"A pessoa viveu {idade_semanas} semanas")
print(f"A pessoa viveu {idade_dias} dias\n")

# 6️⃣ 


