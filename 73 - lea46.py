#prog lea46
num=float(input("\nentre com um numero com parte fracionaria: "))
numi=round(num - 0.5)
numfrac=num-numi
numa=round(num+0.00001)
print(f"\nparte inteira: {numi}")
print(f"\nparte fracionária: {numfrac+0.00001:.3f}")
print(f"\nnumero arredondado: {numa}\n")
