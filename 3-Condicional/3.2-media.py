# Solicitando o nome e a nota do usuário
nome = input ("Digite seu nome: ")
nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))
nota_3 = float(input("Digite sua terceira nota: "))

# Realizando o cálculo da media
media = (nota_1 + nota_2 + nota_3) / 3

print ("A média do Aluno(a)", nome, "é", media)
print (f"A média do aluno(a) {nome} é {media:.2f}")

if media < 4:
    print ("Reprovado")

elif media <= 6:
    print("Recuperação")

else: 
    print("Aprovado")


