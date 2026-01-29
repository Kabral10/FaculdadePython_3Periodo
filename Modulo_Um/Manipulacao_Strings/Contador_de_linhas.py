with open('ManipulandoTexto.txt', encoding='utf-8') as arquivo:
    contador = 0
    print('Representação do arquivo:')
    for line in arquivo:
        print(repr(line))
        if line:
            contador += 1
    print('Total de linhas: ', contador)


#REMOVE ESPAÇOS EM BRANCO
with open('ManipulandoTexto.txt', encoding='utf-8') as arquivo:
    contador_limpo = 0
    print('Representando o arquivo após strip:')
    for line in arquivo:
        line_clean = line.strip()
        print(repr(line_clean))
        if line_clean:
            contador_limpo += 1
    print('Total de linhas limpas: ', contador_limpo)