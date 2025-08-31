# ex018 - Seno, Cosseno e Tangente
ang = float(input("\nDigite o ângulo que você deseja: "))
import math
seno = math.sin(math.radians(ang))  # Seno
cosseno = math.cos(math.radians(ang))  # Cosseno        
tangente = math.tan(math.radians(ang))  # Tangente
print(f"\nO ângulo de {ang}° tem o SENO de {seno:.2f}")
print(f"O ângulo de {ang}° tem o COSSENO de {cosseno:.2f}") 
print(f"O ângulo de {ang}° tem a TANGENTE de {tangente:.2f}\n") 
