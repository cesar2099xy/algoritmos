#prog lea52
p=float(input("\ndigite o valor da aplicação: "))
i=float(input("\ndigite a taxa (O-1): "))
n=int(input("\ndigite o número de meses: "))
va=p*(((1+i)**n)-1)/i
print(f"\nO valor acumulado: {va}\n")
