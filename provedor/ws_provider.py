from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
from produto_service import ProdutoService
from produto import Produto

service = ProdutoService()

class ProdutoHandler(BaseHTTPRequestHandler):
    
    def response_json(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def response_error(self, status_code, message):
        self.response_json(status_code, {"erro": message})

    def get_query_params(self):
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)
        params = {}
        for key, value in qs.items():
            params[key] = value[0] 
        return parsed.path, params

    def do_GET(self):
        path, params = self.get_query_params()

        if path == "/produtos":
            if 'codigo' in params:
                produto = service.buscarPorCodigo(params['codigo'])
                if produto:
                    self.response_json(200, {"produto": produto.to_dict()})
                else:
                    self.response_error(404, "Produto não encontrado")
            else:
                lista = [p.to_dict() for p in service.listarTodos()]
                self.response_json(200, {"produtos": lista})
        else:
            self.response_error(404, "Rota não encontrada")

    def do_POST(self):
        path, params = self.get_query_params()

        if path == "/produtos":
            if 'codigo' not in params:
                self.response_error(400, "Código é obrigatório")
                return

            try:
                codigo = params['codigo']
                nome = params.get('nome')
                preco = float(params['preco']) if params.get('preco') else 0.0
                qtd = int(params['quantidade']) if params.get('quantidade') else 0

                novo_prod = Produto(codigo, nome, preco, qtd)
                resultado = service.criar(novo_prod)

                if resultado:
                    self.response_json(201, {"produto": resultado.to_dict()})
                else:
                    self.response_error(400, "Produto já existe com este código")
            except ValueError:
                self.response_error(400, "Preço deve ser numérico e Quantidade inteiro")
        else:
            self.response_error(404, "Rota não encontrada")

    def do_PUT(self):
        path, params = self.get_query_params()

        if path == "/produtos":
            if 'codigo' not in params:
                self.response_error(400, "Código é obrigatório")
                return

            try:
                codigo = params['codigo']
                nome = params.get('nome')
                preco = float(params['preco']) if params.get('preco') else None
                qtd = int(params['quantidade']) if params.get('quantidade') else None

                prod_atualizar = Produto(codigo, nome, preco, qtd)
                resultado = service.atualizar(prod_atualizar)

                if resultado:
                    self.response_json(200, {"produto": resultado.to_dict()})
                else:
                    self.response_error(404, "Produto não encontrado")
            except ValueError:
                self.response_error(400, "Erro nos tipos de dados (Preço/Quantidade)")
        else:
            self.response_error(404, "Rota não encontrada")


    def do_DELETE(self):
        path, params = self.get_query_params()
        
        if path == "/produtos":
            if 'codigo' not in params:
                self.response_error(400, "Código é obrigatório")
                return
            
            if service.apagar(params['codigo']):
                self.response_json(200, {"mensagem": "Produto apagado com sucesso"})
            else:
                self.response_error(404, "Produto não encontrado")
        else:
            self.response_error(404, "Rota não encontrada")


def run():
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, ProdutoHandler)
    print(f"Servidor rodando em http://127.0.0.1:8081 ...")
    print("Pressione Ctrl+C para encerrar.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor parado.")

if __name__ == "__main__":
    run()