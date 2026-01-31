
print('Abrindo um arquivo!\n')

try:
    open('arquivo,txt', 'r')
    print("Arquivo aberto com sucesso!")

except FileNotFoundError as erro:
    print("O arquivo não existe!")
    print("Descrição: ", erro)
