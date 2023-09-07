import sys
entrada = sys.stdin.readline()
partes = entrada.split(" ")
x = int(partes[0])
y = int(partes[1])


if x == 1:
    x= 4.0
elif x == 2:
    x = 4.50
elif x ==3:
    x=5
elif x==4:
    x=2
elif x==5:
    x=1.50
print(f"Total: R$ {x*y:.2f}")