# ex021 - Verificando as primeiras letras de um texto
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cid = str(input("Digite o nome da cidade em que você nasceu: ").strip())
print (cid[:5].upper() == "SANTO")
# Obs: Poderia ser usado o método startswith() para fazer essa verificação.
# Exemplo: print(cid.upper().startswith("SANTO"))
