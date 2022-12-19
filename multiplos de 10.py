#multiplos de 10

mult = []

print("Os múltiplos de 10 entre 0 e 100 são: ")

for i in range (0,100):
  if i%10 == 0:
    mult.append(i)

print (mult)