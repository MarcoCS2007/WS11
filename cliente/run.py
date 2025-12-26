from ws_client_produto import ProdutoCliente

def exibirMenu():
    print("\n" + "="*50)
    print("MENU - CRUD PRODUTOS")
    print("="*50)
    print("1. Criar novo produto")
    print("2. Buscar produto por código")
    print("3. Listar todos os produtos")
    print("4. Atualizar produto")
    print("5. Apagar produto")
    print("0. Sair")
    print("="*50)

def criarProduto(client: ProdutoCliente):
    print ("\n---CRIAR NOVO PRODUTO---")
    codigo = input("Código: ").strip()

    if not codigo:
        print ("Erro: Código é obrigatório")
        return
    
    nome = input("Nome(opcional): ").strip() or None
    preco_str = input("Preço(opcional): ").strip()
    quant_str = input("Quantidade(opcional): ").strip()

    try:
        preco = float(preco_str) if preco_str else None
        quantidade = int(quant_str) if quant_str else None

        produto_criado = client.criar(codigo, nome, preco, quantidade)
        
        if produto_criado:
            print(f"\n✓ Produto criado com sucesso!")
            exibir_produto(produto_criado)
        else:
            print("Erro: Não foi possível criar (código já existe?).")
            
    except ValueError:
        print("Erro: Preço e Quantidade devem ser números válidos.")
    except Exception as e:
        print(f"Erro ao criar produto: {e}")


def buscarPorCodigo(client: ProdutoCliente):
    print ("\n---BUSCAR PRODUTO POR CÓDIGO---")
    codigo = input("Código: ").strip()

    if not codigo:
        print ("Erro: Código é obrigatório")
        return
    
    try:
        produto = client.buscarPorCodigo(codigo)
        
        if produto:
            print(f"\n Produto encontrado:")
            exibir_produto(produto)
        else:
            print(f"\n Produto com código '{codigo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao buscar produto: {e}")


def listarTodos(client: ProdutoCliente):
    print ("\n---LISTAR TODOS OS PRODUTOS---")

    try:
        produtos = client.listarTodos()
        
        if not produtos:
            print("Nenhum produto encontrado.")
        else:
            print(f"\nTotal de produtos: {len(produtos)}")
            print("-" * 50)
            for i, produto in enumerate(produtos, 1):
                print(f"\n[{i}]")
                exibir_produto(produto)
                print("-" * 50)
    except Exception as e:
        print(f"Erro ao listar produtos: {e}")


def atualizarProduto(client: ProdutoCliente):
    print ("\n---ATUALIZAR PRODUTOS---")
    codigo = input("Código do produto a ser atualizado: ").strip()

    if not codigo:
        print ("Erro: Código é obrigatório")
        return
    
    try:
        produto_existente = client.buscarPorCodigo(codigo)
        
        if not produto_existente:
            print(f"Erro: Produto com código '{codigo}' não encontrado.")
            return
        
        print(f"\nProduto atual:")
        exibir_produto(produto_existente)
        print("\nInforme os novos dados (deixe em branco para manter o valor atual):")
        
        nome = input(f"Nome [{produto_existente.get('nome') or ''}]: ").strip()
        nome = nome if nome else produto_existente.get('nome')
        
        preco_str = input(f"Preço [{produto_existente.get('preco') or ''}]: ").strip()
        quant_str = input(f"Quantidade [{produto_existente.get('quantidade') or ''}]: ").strip()
        preco = float(preco_str) if preco_str else produto_existente.get('preco')
        quantidade = int(quant_str) if quant_str else produto_existente.get('quantidade')
        
        resultado = client.atualizar(codigo=codigo, nome=nome, preco=preco, quantidade=quantidade)
        
        if resultado:
            print(f"\n✓ Produto atualizado com sucesso!")
            exibir_produto(resultado)
        else:
            print("Erro: Não foi possível atualizar o produto.")
            
    except ValueError:
        print("Erro: Digite apenas números válidos para Preço e Quantidade.")
    except Exception as e:
        print(f"Erro ao atualizar produto: {e}")


def apagarProduto(client: ProdutoCliente):
    print ("\n---APAGAR PRODUTOS---")
    codigo = input("Código do produto a ser excluído: ").strip()

    if not codigo:
        print ("Erro: Código é obrigatório")
        return
    
    try:
        produto_existente = client.buscarPorCodigo(codigo)
        
        if not produto_existente:
            print(f"Erro: Produto com código '{codigo}' não encontrado.")
            return
        
        print(f"\nProduto a ser apagado:")
        exibir_produto(produto_existente)
        
        confirmacao = input("\nTem certeza que deseja apagar? (s/N): ").strip().lower()
        
        if confirmacao == 's':
            resultado = client.apagar(codigo)
            
            if resultado:
                print(f"\n✓ Produto apagado com sucesso!")
            else:
                print("Erro: Não foi possível apagar o produto.")
        else:
            print("Operação cancelada.")
    except Exception as e:
        print(f"Erro ao apagar produto: {e}")


def exibir_produto(produto: dict):
    print(f"  Código: {produto.get('codigo', 'N/a')}")
    print(f"  Nome: {produto.get('nome') or 'Não informado'}")
    print(f"  Preço: {produto.get('preco') or 'Não informado'}")
    print(f"  Quantidade: {produto.get('quantidade') or 'Não informado'}")


def main():
    cliente = ProdutoCliente()

    while True:
        exibirMenu()
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            criarProduto(cliente)
        elif opcao == "2":
            buscarPorCodigo(cliente)
        elif opcao == "3":
            listarTodos(cliente)
        elif opcao == "4":
            atualizarProduto(cliente)
        elif opcao == "5":
            apagarProduto(cliente)
        elif opcao == "0":
            print("\nSaindo... Até logo!")
            break
        else:
            print("\n Opção inválida! Tente novamente.")
        
        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()