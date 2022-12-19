#Escreva um progama que verifique se uma entrada já está presente em uma lista

numeros = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def checar(x):
  if x in numeros:
      print('A entrada está presente no dicionário')
  else:
      print('A entrada não está presente no dicionário')
checar(5)
checar(9)