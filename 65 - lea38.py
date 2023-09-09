#prog lea38
import math as m
altura=float(input("\ndigite a altura da lata: "))
raio=float(input("\ndigite o raio da lata: "))
volume=m.pi*raio**2*altura
print(f"\no volume da lata é = {volume:.2f}\n")
