lista_inicial = ["Alice","Letícia","Maria"]

print ("Lista inicial: ",lista_inicial)
print (100 * "-")
#=========Acrescentando item na lista==========
lista_inicial.append("Amélia")
print("Após o append: ", lista_inicial)
print (100 * "-")
#===============Acrescentando item em específico==============
lista_inicial.insert(2,"Luiza")
print("Após o insert()",lista_inicial)
print(100 * "-")
#==========Modificando item da lista========
lista_inicial[1] = "Angela"
print("Após modificação: ",lista_inicial)
print (100 * "-")
#==========Apagando índice específico========
del lista_inicial[1]
print ("Após del: ", lista_inicial)
print( 100 * "-")
#==========Apagando valor específico========
lista_inicial.remove ("Alice")
print("Após remove: ",lista_inicial)
print (100 * "-")
#==========Apagando armazenando valor da lista========
removido = lista_inicial.pop(1)
print(f"Após o pop, removido {removido} ",lista_inicial)
print (100 * "-")
#===========Limpando completamente a lista==========
lista_inicial.clear()
print("Após clear: ",lista_inicial)

