#escreva um programa que encontre a media de tres valores

v1 = float(input("Insira o primeiro numero: "))
v2 = float(input("Insira o segundo numero: "))
v3 = float(input("Insira o terceiro numero: "))

if v1 > v2:
    if v1 < v3:
        media = v1
    elif v2 > v3:
        media = v2
    else:
        media = v3
else:
    if v1 > v3:
        media = v1
    elif v2 < v3:
        media = v2
    else:
        media = v3

print("A media é: ", media)