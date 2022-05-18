usuarios = {}
print (usuarios)
usuarios = {
    "chaves" : ["Chaves do 8", "17/06/2017", "Recep_01"], #criação do dicionário para estrutura de dados
    "quico" : ["Quico das Flores", "03/06/2017", "Raiox_02"]
}
print (usuarios)

usuarios["florinda"] = ["Dona Florinda", "26/11/2017", "Recep_01"] #mostra dados de um usuário, agora incluído no dicionário global
print (usuarios)

print ("----------------------------------------------------")
print (usuarios.get("quico")) #busca dados do usuário em específico