import sqlite3 as conector

# Abertura de conexão
conexao = conector.connect("URL SQLite")

# Aquisição de um cursor
cursor = conexao.cursor()

# Execução de comandos
cursor.execute(...)
cursor.fetchall()

# Efetivação do comando
conexao.commit()

# fechamento das conexões
cursor.close()
conexao.close()