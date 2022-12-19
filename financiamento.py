#financiamento

salario = float (input ("Insira o valor do salário: "))
financiamento = float (input("Insira o valor do financiamento pretendido: "))

if financiamento <= 5 * salario:
    print("Financiamento concedido, obrigado por nos consultar ;)")

else:
    print("Financiamento negado, obrigado por nos consultar ;)")