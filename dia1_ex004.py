# ex004 - Dissecando uma Variável

msg = input('Digite algo: \033[1;32m')
print(f'\033[mO tipo primitivo deste valor é: {type(msg)}')
print(f'Só tem espaços? {msg.isspace()}')
print(f'É um número? {msg.isnumeric()}')
print(f'É alfabético? {msg.isalpha()}')
print(f'É alfanumérico? {msg.isalnum()}')
print(f'Está em maiúsculas? {msg.isupper()}')
print(f'Está em minúsculas? {msg.islower()}')
print(f'Esta capitalizada? {msg.istitle()}')
