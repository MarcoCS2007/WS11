from produto import Produto

class ProdutoService:

    def __init__(self):
        self.__produtos = []

    def buscarPorCodigo(self, codigo: str) -> Produto:
        codigoBusca = codigo.strip().upper()
        for p in self.__produtos:
            if p.codigo.strip().upper() == codigoBusca:
                return p 
        return None

    def criar(self, produto: Produto) -> Produto:
        if self.buscarPorCodigo(produto.codigo):
            print("Erro: Produto já existe!")
            return None
        self.__produtos.append(produto)
        return produto

    def atualizar(self, produto_novo: Produto) -> Produto:
        produto = self.buscarPorCodigo(produto_novo.codigo)
        
        if produto:
            index = self.__produtos.index(produto)
            self.__produtos[index] = produto_novo
            return produto_novo
        
        return None

    def apagar(self, codigo: str) -> bool:
        produto = self.buscarPorCodigo(codigo)
        
        if produto:
            self.__produtos.remove(produto)
            return True            
        return False 

    def listarTodos(self) -> list:
        return self.__produtos 