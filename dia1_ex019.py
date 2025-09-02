# ex019 - Analisador de Textos

nome = input("Digite seu nome: ")
print('Analizando seu nome...')
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras.')
primeiro_nome = nome.split()[0]
print(f'Seu primeiro nome é "{primeiro_nome}" e ele tem {len(primeiro_nome)} letras.')
# Obs: Também poderia ser usado o método replace() para remover os espaços.
