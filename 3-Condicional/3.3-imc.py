# Solicitando informações do usuário
nome = input ("Digite seu nome: ")
peso = float (input ("Digite seu peso kg: "))
altura =  float (input ("Digite sua altura m: "))

# Cálculando o imc do usuário
imc = peso / altura * altura

# Definindo o quadro do usuário segundo ao IMC
if imc < 18.5:
    situacao = "Abaixo do peso"
elif imc <= 24.9:
    situacao = "Peso normal"
elif imc <= 29.9:
    situacao = "Sobrepeso"
elif imc <= 34.9:
    situacao = "Obesidade grau 1"
elif imc <= 39.9:
    situacao = "Obesidade grau 2"
else:
    situacao = "Obesidade grau 3"

    print (f"O IMC do paciente {nome} é {imc} e ele(a) está: {situacao}")