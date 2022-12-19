#Escreva um programa Python para encontrar os números que são divisíveis por 7 e múltiplos de 5, entre 1500 e 2700



nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))