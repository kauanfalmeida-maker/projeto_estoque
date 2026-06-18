# [id, nome, quantidade, localização]

estoque = [
[1, "Amortecedor",3,"Pratileira 01"],
[2, "Fluido de freio",5,"Pratileira 02"],
[3, "Carburador",4,"Pratileira 03"],
[4, "Balança Traseira",6,"Pratileira 04"]
]
for linha in estoque:
 print(linha)


def registrar_produto():
    ##Essa funcao pergunta o nome do tripulante e adiciona na lista de tripulantes
    nomeProduto = input("QUAL O NOME DO PRODUTO?: ")
    idProduto = input("QUAL O ID DO PRODUTO?: ")
    quantidadeProduto = input("QUAL A QUANTIDADE DO PRODUTO?: ")
    localizaçãoProduto = input("QUAL A LOCALIZAÇÃO DO PRODUTO?: ")
    estoque.append([idProduto, nomeProduto, quantidadeProduto, localizaçãoProduto])
    print("RESGISTRO CONCLUIDO! ")

def lista_produtos():
    print("----- PRODUTINHOS -----")
    for linha in estoque:
        print(linha)


def idProduto():
    idProduto = int(input("QUAL O ID DO PRODUTO:"))
    linhaProcurada = -1
    for i in range(len(estoque)):
        if(estoque[i][0] == idProduto):
            linhaProcurada = i
    print(f"O nome procurado é {estoque[linhaProcurada]}")

def atualizarEstoque():
    idProduto = int(input("QUAL O ID DO PRODUTO?:"))
    linhaProcurada = -1
    for i in range(len(estoque)):
        if(estoque[i][0] == idProduto):
            linhaProcurada = i
    
    print(f"O produto atualizado é {estoque[linhaProcurada]}")
    quantidade = int(input("QUAL A QUANTIDADE DO PRODUTO?: "))
    estoque[linhaProcurada][2] = quantidade

while True:
    print("\nBem vindo ao menu do estoque. Por favor selecione uma opção:")
    print("\n1- lista_produtos | 2- idProduto | 3- registrar produto | 4- Atualizar | 5- Sair:")
    opcao = input("Escolha: ")
    if (opcao == "1"):
        lista_produtos()
    elif (opcao == "2"):
        idProduto()
    elif (opcao =="3"):
        registrar_produto()
    elif (opcao =="4"):
        atualizarEstoque()
    elif (opcao =="5"):
     print("Saiu Do Estoque!")
     break
 
  