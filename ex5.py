n1 = float(input("n1:"))
n2 = float(input("n2:"))
n3 = float(input("n3:1"))

if n1 > n2 and n2 > n3:
    print(n1)
elif n3 > n2:
    print(n3)
else:
    print(n2)