#input serve apenas para string, não números. Então se colocado sozinho, armazena nomes, dados que não necessitam de cálculos (como RG, CPF) etc, quando forem números a ser colocados, seguir a estrutura int, float, double juntamente com o input, ex: variavel=int(input("Mensagem a ser digitada: "))
#Por boas práticas, a variável não deve conter espaços nem acentuação, apenas inteira ou separada com _ ou com a segunda palavra junta em Maiúsculo, ex: qtde_funcionarios ou qtdeFuncionarios
nome=input("Digite um funcionário: ") 
empresa=input("Digite a instituição: ")
qtde_funcionarios=int(input("Digite a qtde de funcionários: ")) 
mediaMensalidade=float(input("Digite a média da mensalidade: ")) 
print(nome + " trabalha na empresa " + empresa) #concatenação string com string
print("Possui: ", qtde_funcionarios, " funcionarios.") #concatenação string com números
print("A média da mensalidade é de: " + str(mediaMensalidade))
print("==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variavel [nome] é: ",type(nome)) #função type + nome da variável nos retorna qual o tipo da variavel em questão
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))

