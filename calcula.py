'''Função para calcular a taxa de metabolismo basal'''
def calculadora(atv, peso, altura, sexo, anos):

    if(atv == 'sedentario'):
        fta = 0.988327

    elif(atv == 'leve'):
        fta = 1.1323

    elif(atv == 'moderado'):
        fta = 1.27626

    elif(atv == 'alto'):
        fta = 1.42023

    elif(atv == 'extremo'):
        fta = 1.5655

    else:
        print("erro")

        
    if(sexo == 'h'):
        tbm = float(fta) * (66 + ((13.7 * float(peso)) + (5 * float(altura)) - (6.8 * float(anos))))
        
    elif(sexo == 'm'):
        tbm = float(fta) * (655 + ((9.6 * float(peso)) + (1.8 * float(altura)) - (4.7 * float(anos))))

    else:
        print("erro")
        

    tbm = round(tbm)

    return tbm