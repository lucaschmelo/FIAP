tabuada=int(input("Digite um número maior que 2 e menor que 1000 para exibir a tabuada: "))
if tabuada >= 2 and tabuada <=1000:
    print("Tabuada do número", tabuada)
    for valor in range(0,11,1): #início, fim e incremento
        print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))
else:
    print("Digite um número válido (entre 2 e 1000)")