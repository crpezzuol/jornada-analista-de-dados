# ex008 - Analisando Triângulo v1.0

'''
Escreva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
print('\033[1;32m-=' * 22)
print(' ' * 10 + '\033[1;33mAnalisador de Triângulos')
print('\033[1;32m-=' * 22)
print('\033[m\nDigite o comprimento de três segmentos para saber se eles podem formar um triângulo:\n')
r1 = float(input('Primeiro segmento: \033[1;34m'))
r2 = float(input('\033[mSegundo segmento: \033[1;34m'))
r3 = float(input('\033[mTerceiro segmento: \033[1;34m'))
print('\033[m', end='')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\n\033[1;32mOs segmentos acima PODEM FORMAR um triângulo!\033[m\n')
else:
    print('\n\033[1;31mOs segmentos acima NÃO PODEM FORMAR um triângulo!\033[m\n')

# Teste de existência de um triângulo
# O comprimento de cada lado de um triângulo é menor que a soma dos outros dois lados.
# Exemplo: 7, 5, 3 (7 < 5 + 3) (5 < 7 + 3) (3 < 7 + 5) -> Pode formar um triângulo
# Exemplo: 1, 2, 3 (1 < 2 + 3) (2 < 1 + 3) (3 !< 1 + 2) -> Não pode formar um triângulo
# Referência: https://brasilescola.uol.com.br/matematica/triangulo.htm
# Referência: https://www.todamateria.com.br/triangulo/
# Referência: https://pt.khanacademy.org/math/geometry/hs-geo-triangles/hs-geo-triangle-inequality/a/triangle-inequality
