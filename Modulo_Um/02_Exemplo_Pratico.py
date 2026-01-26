import os

#Abrindo o arquivo no modo escrita
arquivo = open('exemplo.txt', 'w', encoding='utf-8')

#Exibindo os atributos do arquivo
print('nome do arquivo:', arquivo.name)
print('modo de abertura:', arquivo.mode)
print('o arquivo está fechado?', arquivo.closed)

#Escrevendo no arquivo
arquivo.write('Olá, mundo!')

#Fechando o arquivo
arquivo.close()

#Verificando se o arquivo está fechado
print('O arquivo está fechado?',arquivo.closed)

#verificando os caminhos relativos e absolutos
relpath = os.path.relpath('exemplo.txt')
abspath = os.path.abspath('exemplo.txt')

print('Caminho relativo:', relpath)
print('Caminho absoluto:', abspath)