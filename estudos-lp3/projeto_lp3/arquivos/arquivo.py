import os

#ler arquivo
arquivokkj = open("./arquivos/dados.txt")
arquivo2kkj = open("./arquivos/dados.txt")

#pa ler
print(arquivokkj.read())

conteudokkj = arquivo2kkj.read()

print(conteudokkj)

#fecha o bagulho
arquivokkj.close()

#bloco with

#caminho baguiado dinamico
caminho = os.path.join(os.path.dirname(__file__), "dados.txt")

with open("./arquivos/dados.txt", "r") as arquivu:
    linhaskkj = arquivu.readlines()
    print(linhaskkj)
    for i in linhaskkj:
        print(i, end = "")
    print("\n\nboitata")
    #print(arquivu.read())


#--------alterar o arquivo
#modo r- le
#modo w- substitui conteudo
#modo a- coloca, COLOCA
with open("./arquivos/dados.txt", "a") as arquivu:
    arquivu.write("\nbaka")


#com arquivo csv

with open("./arquivos/produtos.csv", "r") as arquivos_produtos:
    produtos = []

    for i in arquivos_produtos:
        dado = i.strip().split(",")
        produto = {
            "nome" : dado[0],
            "descricao" : dado[1]
        }
        produtos.append(produto)

    print(produtos)