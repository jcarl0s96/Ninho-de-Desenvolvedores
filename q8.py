# escreva um programa que multiplique todos os items de uma lista

def multiplicarLista(items):
    total = items[0]
    for x in items:
        total *= x
    return total


print('multiplicação: ',multiplicarLista ([10, 2, -8]))
