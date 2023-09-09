#prog leal5
import math as m
angulo=float(input("\ndigite um angulo em graus: "))
rang = angulo*m.pi/180
print(rang)
print(f"\nseno: {m.sin(rang):.2f}")
print(f"\ncosseno: {m.cos(rang):.2f}")
print(f"\ntangente: {m.tan(rang):.2f}")
print(f"\nco-secante: {1/m.sin(rang):.2f}")
print(f"\nsecante: {1/m.cos(rang):.2f}")
print(f"\ncotangente: {1/m.tan(rang):.2f}\n")


