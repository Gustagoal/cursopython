import sqlite3

# Conecta ou cria um novo banco SQLite
conexao = sqlite3.connect("banco_locais.db")  # arquivo .db real
cursor = conexao.cursor()

# Lê o conteúdo do arquivo SQL
with open("banco_locais.sql", "r", encoding="utf-8") as arquivo_sql:
    sql_script = arquivo_sql.read()

# Executa o script inteiro (cria tabelas e insere dados)
cursor.executescript(sql_script)

# Confirma as alterações
conexao.commit()

# Agora você pode consultar os dados
cursor.execute("SELECT * FROM locais")  # use o nome da tabela do script
dados = cursor.fetchall()

for linha in dados:
    print(linha)

conexao.close()
