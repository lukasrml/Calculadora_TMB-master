from flask import Flask, render_template, request

import sqlite3
from criar_db import *
from data import *
from calcula import *

app = Flask(__name__)


'''Classe global para salvar as informações do usuario logado para utilizalas em qualquer outra função'''
class usuario():
    def nome(self):
        return self.nom
    def email(self):
        return self.ema 
    def senha(self):
        return self.sen 
    def nascimento(self):
        return self.nasc 

    def set_nome(self, nom):
        self.nom = nom
    def set_email(self, ema):
        self.ema = ema
    def set_senha(self, sen):
        self.sen = sen
    def set_nascimento(self, nasc):
        self.nasc = nasc

user = usuario()

'''Inicia a página'''
@app.route("/")
def inicio():
    return render_template("home.html")

'''Verifica se o botão "Criar login" no arquivo home.html foi precionado'''
@app.route("/criarlogin", methods =["POST"])
def criarlogin():
    
    if request.method == "POST":
        '''Redireciona o usuario para página de criação do login'''
        mini = min()
        maxi = max()
        return render_template("criar_login.html", mini = mini, maxi = maxi)


'''Função para registrar as informção do login criado'''
@app.route("/registrar", methods =["POST"])
def registrar():

    if request.method == "POST":
        
        '''Recebe as informações do formulario do arquivo "criar_login.html"'''
        email = request.form["email"]
        nome = request.form["nome"]
        nascimento = request.form["nascimento"]
        senha1 = request.form["senha1"]
        senha2 = request.form["senha2"]

        '''Compara se o usuario digitou a mesma senha'''
        if(senha1 == senha2):
            try:
                senha = senha1

                conn = sqlite3.connect('login.db') 
                c = conn.cursor()

                '''Verifica se o login criado já existe'''
                ver = c.execute("SELECT * FROM user where email = '"+email+"'").fetchall()
                                    
                conn.commit()

                if ver:
                    return render_template("criar_login.html", erro = "Esse login já existe!")

                else:
                    conn = sqlite3.connect('login.db') 
                    c = conn.cursor()

                    '''Salva as informações do novo login'''
                    c.execute("INSERT INTO user VALUES ('"+email+"', '"+nome+"','"+senha+"','"+nascimento+"')")
                                            
                    conn.commit()
                    
                    return render_template("home.html", erro="Login criado com sucesso!")
            
            except Exception as e:
                #print(e)
                raise

        else:
            return render_template("criar_login.html", erro = "Senhas incompativeis!") 
        

'''Função para logar no site'''
@app.route("/logar", methods =["POST"])
def logar():
    
    if request.method == "POST":
        '''Recebe as informações do formulario do arquivo "home.html"'''
        email = request.form["email"]
        senha = request.form["senha"]

        '''Redireciona essas infirmações para uma outra função para verificar se o login existe'''
        return login(email, senha)
    

'''Função para verificar o login'''
def login(email, senha):

    try:
        conn = sqlite3.connect('login.db') 
        c = conn.cursor()

        '''Verifica se o login está salvo no banco de dados "user"'''
        log = c.execute("SELECT * FROM user where email = '"+email+"' and senha ='"+senha+"'").fetchall()
                            
        conn.commit()

        if log:
            '''Redireciona o usuario para a pagina principal caso o login exista'''
            peganome = c.execute("SELECT nome FROM user where email = '"+email+"'").fetchall()
            nome = str(peganome)
            nome = nome[3:-4]
            peganasc = c.execute("SELECT nascimento FROM user where email = '"+email+"'").fetchall()
            nasc = str(peganasc)

            '''Salva as informações fornecidas pelo usuario no resgistro em uma classe global para disponibilizalas para uso em outras funções'''
            user.set_nome(nome)
            user.set_email(email)
            user.set_senha(senha)
            user.set_nascimento(nasc[3:-4])

            return render_template("calcula.html", nome = nome)
        
        else:
            return render_template("home.html", erro="Esse login não existe!")

    except Exception as e:
        #print(e)  
        raise 


'''Função que recebe os valores para o calculo e chama a operação'''
@app.route("/calcular", methods =["POST"])
def calcular():

    if request.method == "POST":

        sexo = request.form["sexo"]
        peso = request.form["peso"]
        altura = request.form["altura"]
        atv = request.form["atv"]

        nasc = user.nascimento()

        anos = idade(nasc)

        tbm = calculadora(atv, peso, altura, sexo, anos)

        pp = tbm - 500
        gp = tbm + 500

        tbm = str(tbm)+" kcal"

        return render_template("calcula.html", tbme = tbm, nome = user.nome(), pp = pp, gp = gp)



app.run()
