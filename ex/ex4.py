velocidade = int(input("velocidade"))
multa= 0
if velocidade>80:
    velocidade=velocidade-80
    multa = velocidade*5
print(multa)