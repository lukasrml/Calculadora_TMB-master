import sqlite3

conn = sqlite3.connect('login.db') 
c = conn.cursor()

'''Cria um banco de dados chamado "user", caso ainda não exista'''
c.execute('''
CREATE TABLE IF NOT EXISTS user
([email] STRING PRIMARY KEY, [nome] STRING, [senha] STRING, [nascimento] STRING);
''')