#maior número

i = 0
maior = 0

print ("Insira 0 para quando quiser finalizar")

valor = float (input ("Digite um número positivo maior que zero: "))

while valor != 0:
    valor = float(input("Digite um número positivo maior que zero: "))
   
if valor > maior:
        maior = valor

print ("O maior valor digitado foi: ", maior)