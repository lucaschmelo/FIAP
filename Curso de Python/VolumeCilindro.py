import math
resposta = "S"
while resposta == "S":
    aluno=(input("\nAluno: "))
    altura=(float(input("Altura do cilindro: ")))
    raio=(float(input("Raio do cilindro: ")))
    volume=math.pi*raio*raio*altura
    print("-----------------------------------------")
    print("Volume do cilindro: ", volume)
    resposta = input("\nDigite \"S\" para continuar incluindo alunos ou \"ENTER\" para finalizar: ").upper()