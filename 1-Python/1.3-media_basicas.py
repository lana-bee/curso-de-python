# Criando a variável nome e as variáveis notas
nome = input (" Nome do Aluno: ")
nota_1 = float (input ("1 Bimestre:"))
nota_2 = float (input ("2 Bimestre: "))
nota_3 = float (input ("3 Bimestre: "))

# Calculando a média do Aluno 
media = nota_1 + nota_2 + nota_3  / 3

# Apresentando as notas do 
print ("A média do Aluno(a)", nome, "é", media)