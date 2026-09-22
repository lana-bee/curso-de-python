# Coletando renda em situação do correntista
renda = float (input ("Digite sua renda mensal R$"))
situacao = input ("Possuiu restrição / nome negativado (s/n): ")

# Validando renda e situação de restrição
emprestimo = (renda >= 3000) and situacao == "n"

print ("Emprestimo Aprovado: ", emprestimo)