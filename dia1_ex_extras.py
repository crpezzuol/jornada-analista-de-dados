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
# * 5% de desconto;
# * 10% de desconto;
# * 20% de desconto.

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
# * Quantos meses ela viveu;
# * Quantas semanas;
# * Quantos dias (considerando 365 dias por ano).

print("5️⃣  Conversor de Idade:\n")
idade_anos = int(input("Digite a idade da pessoa em anos: \033[1;32m "))
idade_meses = idade_anos * 12
idade_semanas = idade_anos * 52
idade_dias = idade_anos * 365
print(f"\033[m\nA pessoa viveu {idade_meses} meses")
print(f"A pessoa viveu {idade_semanas} semanas")
print(f"A pessoa viveu {idade_dias} dias\n")

# 6️⃣ **Hipotenusa de um Triângulo Retângulo**
# Peça os dois catetos e calcule a hipotenusa (use a fórmula de Pitágoras).

print("6️⃣  Hipotenusa de um Triângulo Retângulo:\n")
import math # Importando a biblioteca math para usar a função sqrt
cateto1 = float(input("Digite o valor do primeiro cateto: \033[1;32m "))
cateto2 = float(input("\033[mDigite o valor do segundo cateto: \033[1;32m "))
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
print(f"\033[m\nA hipotenusa do triângulo retângulo com catetos {cateto1} e {cateto2} é {hipotenusa:.2f}\n")

# 7️⃣ **Conversor de Minutos para Horas e Minutos**
# Peça ao usuário um valor em minutos e converta para horas e minutos restantes.
# Exemplo de entrada: 135
# Saída esperada:
# - Horas: 2
# - Minutos restantes: 15

print("7️⃣  Conversor de Minutos para Horas e Minutos:\n")
total_minutos = int(input("Digite o total de minutos: \033[1;32m "))
horas = total_minutos // 60 # Divisão inteira para obter horas completas
minutos_restantes = total_minutos % 60 # Resto da divisão para obter minutos restantes
print(f"\033[m\nHoras: {horas}")
print(f"Minutos restantes: {minutos_restantes}\n") 

# 8️⃣ **Analisador de Nome**
# Peça o nome completo de uma pessoa e mostre:
# * O nome em maiúsculas;
# * O nome em minúsculas;
# * Quantas letras ao todo (desconsiderando espaços);
# * Quantas letras tem o primeiro nome.

print("8️⃣  Analisador de Nome:\n")
nome_completo = input("Digite o nome completo: \033[1;32m ").strip()
nome_maiusculas = nome_completo.upper() # Nome em maiúsculas
nome_minusculas = nome_completo.lower() # Nome em minúsculas
letras_sem_espacos = len(nome_completo.replace(" ", "")) # Contagem de letras sem espaços
primeiro_nome = nome_completo.split()[0] # Obtendo o primeiro nome  
letras_primeiro_nome = len(primeiro_nome) # Contagem de letras do primeiro nome
print(f"\033[m\nNome em maiúsculas: {nome_maiusculas}")
print(f"Nome em minúsculas: {nome_minusculas}")
print(f"Quantidade de letras (sem espaços): {letras_sem_espacos}")
print(f"Quantidade de letras no primeiro nome: {letras_primeiro_nome}\n")

# 9️⃣ **Preço do Combustível**
# Peça quantos litros de combustível foram abastecidos e o preço por litro.
# E mostre o valor total a pagar.

print("9️⃣  Preço do Combustível:\n")
litros = float(input("Digite a quantidade de litros abastecidos: \033[1;32m "))
preco_litro = float(input("\033[mDigite o preço por litro: \033[1;32m R$ "))
total_a_pagar = litros * preco_litro # Cálculo do valor total a pagar
print(f"\033[m\nO valor total a pagar por {litros} litros a R$ {preco_litro:.2f} por litro é R$ {total_a_pagar:.2f}\n") 

# 🔟 
