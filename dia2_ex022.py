# ex022 - Tabuada v.2.0

'''
Refaça o  exercicio dia1_ex009.py, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''

# importando as bibliotecas necessárias
import os
from time import sleep

# limpando a tela
os.system('cls' if os.name == 'nt' else 'clear')

# cabeçalho
print('\n'*3)
print('\033[1;31m=' * 24, '\033[3;34mTABUADA', '\033[1;31m=' * 24)
print('\n\033[m')

# entrada de dados
num = int(input('\033[3;34mDigite um número para ver sua tabuada: \033[1;32m'))
print('\n')

# processamento e saída de dados
sleep(0.5)  # Atraso de 0.5 segundos antes de iniciar a tabuada
print(' ' * 19, 16 * '\033[1;35m-')
for c in range(1, 11):
    print(' ' * 21, f'\033[3;34m{num} X {c:2} = \033[1;32m{num * c:3}')
    sleep(0.3)  # Atraso de 0.3 segundos entre os números
print(' ' * 19, 16 * '\033[1;35m-')

# finalização
print('\n\033[m')
print('\033[1;31m=' * 20, '\033[3;34mFIM DA TABUADA', '\033[1;31m=' * 21)
print('\n' * 3, '\033[m')

# Obs: Os códigos de cores ANSI podem não funcionar em alguns terminais ou IDEs.
# Eles funcionam corretamente em terminais que suportam ANSI, como o terminal do Linux e o PowerShell do Windows.
# Se estiver usando um ambiente que não suporta ANSI, você pode remover os códigos de cores para evitar caracteres estranhos na saída.
# Códigos de cores ANSI usados:
# \033[1;31m - Vermelho forte (negrito)
# \033[3;34m - Azul claro (itálico)
# \033[1;32m - Verde forte (negrito)
# \033[1;35m - Roxo forte (negrito)
# \033[m - Resetar para a cor padrão
# :D - Formatação para alinhar os números na saída
# :2 - Formatação para alinhar os números na saída
# :3 - Formatação para alinhar os números na saída
# :> - Formatação para alinhar os números na saída
# :< - Formatação para alinhar os números na saída
# :^ - Formatação para alinhar os números na saída
# :0 - Formatação para alinhar os números na saída
# :b - Formatação para alinhar os números na saída
# :x - Formatação para alinhar os números na saída
# :X - Formatação para alinhar os números na saída
# :o - Formatação para alinhar os números na saída
# fim do código
