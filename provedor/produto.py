class Produto:
    def __init__(self, codigo: str, nome: str, preco: float, quantidade: int):
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        self.__preco = valor
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, valor):
        self.__quantidade = valor
    
    def to_dict(self):
        return {
            "codigo": self.__codigo,
            "nome": self.__nome,
            "preco": self.__preco,
            "quantidade": self.__quantidade
        }