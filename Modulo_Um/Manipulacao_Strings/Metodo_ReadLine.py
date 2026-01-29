arquivo = open('ManipulandoTexto.txt', 'r', encoding='utf-8')

coteudo = arquivo.readline()

print('Tipo de conteudo: ', type(coteudo))

print('Conteudo retornado pelo ReadLine:')

print(repr(coteudo))

ProximoConteudo = arquivo.readline()

print('Proximo conteudo retornado pelo ReadLine:')

print(repr(ProximoConteudo))

ProximoConteudo = arquivo.readline()

print('Proximo conteudo retornado pelo ReadLine:')

print(repr(ProximoConteudo))

ProximoConteudo = arquivo.readline()

print('Proximo conteudo retornado pelo ReadLine:')

print(repr(ProximoConteudo))

ProximoConteudo = arquivo.readline()

print('Proximo conteudo retornado pelo ReadLine:')

print(repr(ProximoConteudo))

