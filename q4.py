#Escreva um progama que some todos os items em uma lista

def somarLista (items):
    somaNumeros = 0
    for x in items:
       somaNumeros += x
    return somaNumeros

print (somarLista ([10,50,-8]))