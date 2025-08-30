# ex008 - Conversor de Medidas
mts = float(input("\nDigite a distância em metros: "))
print(f"\nA distância de {mts:.2f} metros corresponde a:")
print(f"{mts / 1000:.3f} km")
print(f"{mts / 100:.2f} hm")
print(f"{mts / 10:.2f} dam")
print(f"{mts * 10:.0f} dm")
print(f"{mts * 100:.0f} cm")
print(f"{mts * 1000:.0f} mm\n")
