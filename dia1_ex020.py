# ex020 - Separando dígitos de um número
num = int(input('Informe um número entre 0 e 9999: '))
print(f'Analisando o número {num}...')
u = num // 1 % 10  # Unidade
d = num // 10 % 10  # Dezena
c = num // 100 % 10  # Centena
m = num // 1000 % 10  # Milhar
print(f'Unidade: {u}')  # Imprime a unidade do número
print(f'Dezena: {d}')  # Imprime a dezena do número
print(f'Centena: {c}')  # Imprime a centena do número
print(f'Milhar: {m}')  # Imprime o milhar do número
# Obs: Também poderia ser feito convertendo o número para string e acessando cada índice.
