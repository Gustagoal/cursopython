import sqlite3

conexao = sqlite3.connect("banco_novo")

cursor = conexao.cursor()

# cursor.execute('CREATE TABLE teste(nome,idade,trabahlo)')

consulta = cursor.execute('SELECT * FROM teste  ').fetchall()

print(consulta)