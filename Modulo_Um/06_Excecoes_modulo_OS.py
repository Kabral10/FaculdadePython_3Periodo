import os

def processar_arquivo(arquivo_origem, arquivo_destino):

    try:
        with open(arquivo_origem, 'r', encoding='utf-8') as f_origem:
            content = f_origem.read()
    except FileNotFoundError as error:
        print(f"Arquivo {arquivo_origem} não encontrado.")
        print(f"Erro: {error}")
        return
    except PermissionError as error:
        print(f'Sem permissão para ler {arquivo_origem}.')
        print(f'Erro: {error}')
        return
    except Exception as error:
        print(f'Erro inesperado ao ler {arquivo_origem}.')
        print(f'Erro: {error}')
        return

    try:
        with open(arquivo_destino, 'w', encoding='utf-8') as f_destino:
            f_destino.write("Cabeçalho: Conteúdo do arquivo\n")
            f_destino.write(content)
            print(f'Conteúdo escrito em {arquivo_destino}.')
    except PermissionError as error:
        print(f'Sem permissão para abrir o arquivo {arquivo_destino}.')
        print(f'Erro: {error}')
    except Exception as error:
        print(f'Erro inesperado ao ler {arquivo_destino}.')
        print(f'Erro: {error}')

def main():
    diretorio_testeOS = '06_diretorio_testeOS'
    arquivo_origem = os.path.join(diretorio_testeOS, 'arquivo_origem.txt')
    arquivo_destino = os.path.join(diretorio_testeOS, 'arquivo_destino.txt')

    processar_arquivo(arquivo_origem, arquivo_destino)

if __name__ == '__main__':
    main()