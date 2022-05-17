import math
resposta = "S"
while resposta == "S":
    aluno=(input("\nAluno: "))
    altura=(float(input("Digite a altura do cilindro: ")))
    raio=(float(input("Digite o raio do cilindro: ")))
    volume=math.pi*raio*raio*altura
    print("Volume do cilindro: ", volume)
    resposta = input("\nDigite \"S\"para continuar incluindo alunos ou \"QUALQUER TECLA\" para finalizar: ").upper()