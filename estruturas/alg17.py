nome = input("Qual o seu nome? ")
turma = input("Qual sua turma? ")


nota1 = float(input("Qual sua primeira nota? "))
nota2 = float(input("Qual sua segunda nota? "))
nota3 = float(input("Qual sua terceira nota? "))
nota4 = float(input("Qual sua quarta nota? "))


media = (nota1 + nota2 + nota3 + nota4) / 4


print(f"Olá, {nome}!")
print(f"Sua turma é: {turma}")
print(f"Sua média é: {media:.1f}")  


if media >= 70:
    print(f"Parabéns {nome}, você foi aprovado!")
else:
    print(f"Que pena {nome}, você foi reprovado.")
    
