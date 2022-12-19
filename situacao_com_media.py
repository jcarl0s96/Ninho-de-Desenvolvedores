#situação com média

n1 = float(input("Insira a 1ª nota: "))
n2 = float(input("Insira a 2ª nota: "))
n3 = float(input("Insira a 3ª nota: "))
n4 = float(input("Insira a 4ª nota: "))
media = (n1 + n2 + n3 + n4)/4

if media >= 5:
    print(f"O aluno foi aprovado com a média {media:.2f}")
else:
    print(f"O aluno foi reprovado com a média {media:.2f}")