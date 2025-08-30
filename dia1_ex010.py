# ex010 - Conversor de Moedas
moeda = float(input('\nQuanto dinheiro você tem na carteira? R$ '))
print(f'Com R$ {moeda:.2f} reais você pode comprar US$ {moeda / 5.43:.2f} dólares.\n')
# Considerando a cotação do dólar a R$ 5,43 do dia 30/08/2025.
# Cotação atual pode variar, verifique a cotação atual para valores precisos.
# Fonte da cotação: https://www.google.com/search?q=cotação+dólar+hoje
