import sys

entrada1 = sys.stdin.readline()
entrada2 = sys.stdin.readline()

parte1 = entrada1.split(" ")
q1 = int(parte1[1])
v1 = float(parte1[2])

parte2 = entrada2.split(" ")
q2 = int(parte2[1])
v2 = float(parte2[2])

valor = (q1*v1) + (q2*v2)
print(f"VALOR A PAGAR: R$ {valor:.2f}")
