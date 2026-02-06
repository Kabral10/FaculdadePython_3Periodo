import sqlite3

conexao = sqlite3.connect('./meu_banco.db')
cursor = conexao.cursor()

comando = '''SELECT nome, oculos FROM Pessoa;'''
cursor.execute(comando)

registros = cursor.fetchall()
print('Tipo retornado pelo fetchall(): ', type(registros))

for registro in registros:
    print('tipo:', type(registro), '- conteudo:', registro)

cursor.close()
conexao.close()