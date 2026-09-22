# Solicitando idade e se é estudante
idade = int(input("Digite a sua idade: "))
estudante = input("Você é estudante s/n: ")

# Validando meia entrada
meia = (idade >= 60) or estudante == "s"

# Apresentando o resultado ao usuário
print ("Parabéns! você tem direito a meia-entrada ", meia )