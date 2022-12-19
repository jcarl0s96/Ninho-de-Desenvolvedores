#escreva um programa que receba do usuario uma palavra e a inverta

palavra = input("Insira uma palavra e veja seu reverso: ")

for char in range(len(palavra) - 1, -1, -1):
  print(palavra[char], end="")

