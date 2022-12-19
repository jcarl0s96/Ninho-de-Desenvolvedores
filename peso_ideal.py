#peso ideal

altura = float (input ("Digite sua altura em metros: "))
sexo = input ("Você é do sexo masculino ou feminino? ")
peso = 0

if sexo == "feminino":
    peso = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é: {peso: .2f} KG")
elif sexo == "masculino":
    peso = (72.7 * altura) - 58
    print(f"Seu peso ideal é: {peso: .2f} KG")
else:
    print("Digite um sexo válido")