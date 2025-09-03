# ex025 - Procurando uma string dentro de outra.
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input("Digite seu nome completo: ").strip())
print("Analisando seu nome...")
print("Seu nome tem Silva?", "SILVA" in nome.upper())
# Obs: Poderia ser usado o método find() para fazer essa verificação.
# Exemplo: print(nome.upper().find("SILVA") != -1)
