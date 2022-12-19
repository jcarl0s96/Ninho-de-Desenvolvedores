#Escreva um programa  para contar a frequencia em que um caractere aárece em uma string

def carcactereF(str1):
    dict = {}
    for n in str1:
        entrada = dict.keys()
        if n in entrada:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(carcactereF('gato_pingado'))