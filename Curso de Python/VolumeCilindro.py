import math
resposta = "S"
for resposta in range (1,6):
    aluno=(input("\nAluno: "))
    altura=(float(input("Altura do cilindro: ")))
    raio=(float(input("Raio do cilindro: ")))
    volume=math.pi*raio*raio*altura
    print("-----------------------------------------")
    print("Volume do cilindro: ", volume)
    resposta = input("\nAperte enter para continuar incluindo alunos (limite de 5 alunos) ").upper()