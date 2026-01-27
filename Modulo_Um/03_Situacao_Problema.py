#Você foi contratado por uma editora para desenvolver um programa que ajude na revisão de textos.
#A editora recebe frequentemente textos de autores que contêm inconsistências no uso de maiúsculas e minúsculas,
#o que dificulta o processo de edição e publicação.


def main():
    print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo. ")
    frases = []
    while True:
        entrada = input("> ")
        if entrada.lower() == 'sair':
            break
        frases.append(entrada)

    with open('03_Problema.txt', 'w') as arquivo:
        for frase in frases:
            arquivo.write(frase + '\n')

    print("Arquivo original criado com sucesso! Hora de manipular os dados!\n")
    dados_modificados = []
    with open('03_Problema.txt', 'r') as arquivo:
        for linha in arquivo:
            dados_modificados.append(linha.strip().upper())

    with open('03_Problema.txt', 'w') as arquivo:
        for linha in dados_modificados:
            arquivo.write(linha + '\n')

    print("O arquivo foi sobrescrito com os dados modificados!")

if __name__ == '__main__':
    main()