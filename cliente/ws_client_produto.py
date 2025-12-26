import requests

class ProdutoCliente:
    def __init__(self):
        self.base_url = "http://localhost:8081"
        self.url_completa = f"{self.base_url}/produtos"

    def buscarPorCodigo(self, codigo: str) -> dict:
        response = requests.get(self.url_completa, params={"codigo": codigo})
        if response.status_code == 404:
            return None
        dados_json = response.json()
        return dados_json.get('produto', None)
    
    def listarTodos(self) -> list:
        try:
            response = requests.get(self.url_completa)
            if response.status_code != 200:
                return []
            dados_json = response.json()
            return dados_json.get('produtos', [])
        except:
            return []

    def criar(self, codigo: str, nome: str = None, preco: float = None, quantidade: int = None) -> dict:
        params = {"codigo": codigo}
        if nome:
            params["nome"] = nome
        if preco is not None:
            params["preco"] = str(preco)
        if quantidade is not None:
            params["quantidade"] = str(quantidade)

        response = requests.post(self.url_completa, params=params)
        if response.status_code == 201:
            return response.json().get('produto', {})
        return None

    def atualizar(self, codigo: str, nome: str = None, preco: float = None, quantidade: int = None) -> dict:
        params = {"codigo": codigo}
        if nome:
            params["nome"] = nome
        if preco is not None:
            params["preco"] = str(preco)
        if quantidade is not None:
            params["quantidade"] = str(quantidade)

        response = requests.put(self.url_completa, params=params)
        if response.status_code == 200:
            return response.json().get('produto', None)
        return None

    def apagar(self, codigo: str) -> bool:
        params = {"codigo": codigo}
        response = requests.delete(self.url_completa, params=params)
        
        if response.status_code == 404:
            return False
        if response.status_code == 200:
            return True
        return False