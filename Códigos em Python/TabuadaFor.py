tabuada=int(input("Digite um número maior que 2 e menor que 1000 para exibir a tabuada: "))
print("Tabuada do número", tabuada)
for valor in range(0,11,1): #início, fim e incremento
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))