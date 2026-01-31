import sqlite3 as conector

#abertura de conexao
conexao = conector.connect('./meu_banco.db')
cursor = conexao.cursor()

#Execução de comandos: SELECT... CREATE...
comando = '''ALTER TABLE Veiculo
                    ADD motor REAL;'''

cursor.execute(comando)

#efetivação
conexao.commit()

#fechamento
cursor.close()
conexao.close()