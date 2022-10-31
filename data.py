from datetime import datetime

'''Função para determinar o valor minimo da date permitida no registro, sendo esse de 100 antes do mês de quando o programa é rodado'''
def min():

    hoje = datetime.now()
    anohj = hoje.year
    meshj = hoje.month

    if(float(meshj) < 10):
        meshj = '0'+meshj

    else:
        print("erro")

    anomin = anohj - 100

    datamin = str(anomin)+'-01'

    return datamin


'''Função para determinar o valor máximo da date permitida no registro, sendo esse de 100 antes do mês de quando o programa é rodado'''
def max():
    hoje = datetime.now()
    anohj = hoje.year
    meshj = hoje.month

    if(float(meshj) < 10):
        meshj = '0'+meshj

    else:
        print("erro")

    datamax = str(anohj)+'-'+str(meshj)

    return datamax


'''Função para determina a idade do ususario com base no mes e ano informados por ele no registro'''
def idade(nasc):
    hoje = datetime.now()
    anonasc = nasc[:4]
    mesnasc = nasc[5:7]
    
    anohj = hoje.year
    meshj = hoje.month

    idade = float(anohj)-float(anonasc)

    dife =  float(meshj) - float(mesnasc)

    if(-6 <= float(dife) < 6):
        idade = idade

    elif(float(dife) > 6):
        idade = float(idade) + 1

    elif(float(dife) < -6):
        idade = float(idade) - 1

    else:
        print("erro")
    
    return idade


