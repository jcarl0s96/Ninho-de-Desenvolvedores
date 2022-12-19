#escreva uma funcao que exiba o me menor valor de uma lista

def menor_numero( lista ):
    min = lista [ 0 ] 
    for a in lista:
        if a < min:
            min = a
    return min
print(menor_numero([10,52,89,100,5]))