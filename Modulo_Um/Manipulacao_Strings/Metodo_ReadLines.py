arquivo = open('ManipulandoTexto.txt', 'r', encoding='utf-8')

conteudo = arquivo.readlines()

print('Tipo de conteudo: ', type(conteudo))

print('Conteudo retornado pelo ReadLines:')

print(repr(conteudo))

arquivo.close()