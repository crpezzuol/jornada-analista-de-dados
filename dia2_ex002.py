# ex002 - Radar eletrônico
# Este programa verifica a velocidade de um carro e calcula a multa se necessário.
# O limite de velocidade é de 80 km/h e a multa é de R$ 7 por km/h acima do limite.
# Exemplo de condição simples, sem else.

vel = int(input("Qual é a velocidade atual do carro em km/h?: "))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você foi multado! Você excedeu o limite permitido que é de 80km/h.')
    print(f'Você deve pagar uma multa de R$ {multa:.2f}!')
print('Tenha cuidado! E dirija com segurança!')
