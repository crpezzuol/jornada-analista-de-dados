# ex014 - Conversor de Temperaturas
# Solicita a temperatura em Celsius
temp = float(input("\nInforme a temperatura em °C: "))
# Converte Celsius em Fahrenheit 
temp_f = (temp * 9/5) + 32
print(f"A temperatura de {temp}°C corresponde a {temp_f:.1f}°F\n")
