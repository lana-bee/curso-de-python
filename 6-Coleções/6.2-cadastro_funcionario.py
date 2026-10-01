# Criando dicionário composto de cadastro de funcionário
funcionarios = {
  "44356":{"nome":"Alana Gomes",
           "telefone":"1197145590",
            "data_nascimento":"15/05/2010",
             "cargo":"Gerente",
             "habilidades":["Prestativa,Comunicativa,,Senso de liderança"]                  
            },
 "42257":{
           "nome":"Rebeca Andrade",
           "telefone":"115500987",
            "data_nascimento":"15/07/1999",
             "cargo":"Atendente",
             "habilidades":["Prestativa,Comunicativa,Organizada"]                  




            },
"22445":{
    "nome":"Flavio Elendre",
           "telefone":"1140123405",
            "data_nascimento":"23/09/1998",
             "cargo":"Chefe",
             "habilidades":["Senso de liderança,Paciente,Inteligente"]                 

    
}


}  

print (funcionarios["22445"]["habilidades"][1])