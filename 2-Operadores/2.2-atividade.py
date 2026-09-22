# Solicitando a altura e idade do usuário
idade = float(input ("Digite sua idade: "))
altura = float (input ("Digite sua altura (m): "))

# Validando as informações
entrada = (idade >= 12) and (altura >= 1.40 )

# Gerando o resultado ao usuário
print ("Você pode andar na nossa montanha-russa", entrada)