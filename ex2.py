def main():
    produtos = []

    while True:
        print("\nOpções:")
        print("1 - Inserir produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("0 - Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            adicionar_produto(produtos)
        elif choice == '2':
            listar_produtos(produtos)
        elif choice == '3':
            atualizar_produto(produtos)
        elif choice == '4':
            deletar_produto(produtos)
        elif choice == '0':
            break
        else:
            print("Opção inválida. Escolha novamente.")

def adicionar_produto(produtos):
    try:
        codigo = input("Código do produto: ")
        descricao = input("Descrição do produto: ")
        quantidade = int(input("Quantidade em estoque: "))
        valor = float(input("Valor do produto: "))

        produto = {
            'Código': codigo,
            'Descrição': descricao,
            'Quantidade': quantidade,
            'Valor': valor
        }

        produtos.append(produto)
        print("Produto adicionado com sucesso.")
    except ValueError:
        print("Erro: Valor inválido para quantidade ou valor.")
    except Exception as e:
        print(f"Erro: {e}")

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for idx, produto in enumerate(produtos, start=1):
            print(f"\nProduto {idx}:")
            print(f"Código: {produto['Código']}")
            print(f"Descrição: {produto['Descrição']}")
            print(f"Quantidade: {produto['Quantidade']}")
            print(f"Valor: {produto['Valor']}")

def atualizar_produto(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        codigo = input("Digite o código do produto a ser atualizado: ")
        encontrado = False

        for produto in produtos:
            if produto['Código'] == codigo:
                encontrado = True
                print(f"Produto encontrado:\nDescrição: {produto['Descrição']}")

                try:
                    quantidade = int(input("Nova quantidade em estoque: "))
                    valor = float(input("Novo valor do produto: "))

                    produto['Quantidade'] = quantidade
                    produto['Valor'] = valor
                    print("Produto atualizado com sucesso.")
                except ValueError:
                    print("Erro: Valor inválido para quantidade ou valor.")
                except Exception as e:
                    print(f"Erro: {e}")

        if not encontrado:
            print("Produto não encontrado.")

def deletar_produto(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        codigo = input("Digite o código do produto a ser deletado: ")
        removido = False

        for produto in produtos[:]:
            if produto['Código'] == codigo:
                produtos.remove(produto)
                removido = True
                print("Produto removido com sucesso.")

        if not removido:
            print("Produto não encontrado.")

if __name__ == "__main__":
    main() 
