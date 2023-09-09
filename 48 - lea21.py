#prog lea21
sm=float(input("\nentre com o salário mínimo: "))
qtdade=float(input("\nentre com a quantidade em quilowatt: "))
# divide por 7 para achar o preço de 100 Kw e por 100 para achar de 1 Kw
preco=sm/700
vp=preco*qtdade
vd=vp*0.9
print(f"\npreço do quilowatt: {preco:.2f}\nvalor a ser pago: {vp:.2f}\nvalor com desconto: {vd:.2f}\n")