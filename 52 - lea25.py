#prog lea25
import math as m
lado=float(input("\ndigite o lado do quadrado: "))
perimetro=4*lado
area=lado**2
diagonal=lado*m.sqrt(2)
print(f"\nperimetro: {perimetro}\narea: {area}\ndiagonal: {diagonal}\n")
