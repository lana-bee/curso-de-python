# Solicitando peso e altura ao usuário
peso = float(input ("digite seu peso (kg): "))
altura = float(input ("digite sua altura (m): "))

imc = peso / altura**2  

# Apresentando o resultado do IMC ao usuário

print ("O seu IMC é", imc)