#prog 1ea23
import math as m
base=float(input("\ndigite base: "))
altura=float(input("\ndigite a altura: "))
perimetro=2*(base + altura)
area=base*altura
diagonal=m.sqrt(base**2+altura**2)
print(f"\nperimetro = {perimetro}\narea = {area}\ndiagonal = {diagonal}\n")

