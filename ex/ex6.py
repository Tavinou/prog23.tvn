salario = int(input("digite salario:"))

if salario > 1250:
    salario_aumento = ((salario*10)/100)
    salario_aumento = salario_aumento + salario
    print(salario_aumento)
elif salario <= 1250:
    salario_aumento = ((salario*15)/100)
    salario_aumento = salario_aumento + salario
    print(salario_aumento)