"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

class CarregadorDetalhesFilme:
    def carregar_detalhes(self, filme):
        raise NotImplementedError


class CarregadorAPIFilme(CarregadorDetalhesFilme):
    def carregar_detalhes(self, filme):
        print(f"[API] Carregando detalhes para {filme.titulo} ({filme.ano})...")
        filme.sinopse = "Um filme incrível vindo de uma API."
        filme.elenco = ["Ator 1", "Atriz 2"]
        filme.capa = "url_da_capa_api.jpg"


class CarregadorBancoFilme(CarregadorDetalhesFilme):
    def carregar_detalhes(self, filme):
        print(f"[BD] Carregando detalhes para {filme.titulo} ({filme.ano})...")
        filme.sinopse = "Um filme armazenado no banco de dados."
        filme.elenco = ["Ator X", "Atriz Y"]
        filme.capa = "url_da_capa_bd.jpg"


class Filme:
    def __init__(self, titulo, ano, carregador_detalhes):
        self.titulo = titulo
        self.ano = ano
        self._carregador_detalhes = carregador_detalhes

        # atributos “pesados” – inicialização tardia
        self.sinopse = None
        self.elenco = None
        self.capa = None
        self._detalhes_carregados = False

    def carregar_detalhes(self):
        if not self._detalhes_carregados:
            self._carregador_detalhes.carregar_detalhes(self)
            self._detalhes_carregados = True

    def mostrar_detalhes(self):
        self.carregar_detalhes()
        print(f"Título: {self.titulo} ({self.ano})")
        print(f"Sinopse: {self.sinopse}")
        print(f"Elenco: {', '.join(self.elenco)}")
        print(f"Capa: {self.capa}")


if __name__ == "__main__":
    # catálogo rápido: só título e ano
    carregador_api = CarregadorAPIFilme()
    carregador_bd = CarregadorBancoFilme()

    catalogo = [
        Filme("Filme da API", 2024, carregador_api),
        Filme("Filme do Banco", 2020, carregador_bd),
    ]

    print("Lista inicial (somente títulos):")
    for filme in catalogo:
        print(f"- {filme.titulo} ({filme.ano})")

    print("\nUsuário clicou no primeiro filme:\n")
    catalogo[0].mostrar_detalhes()

    print("\nUsuário clicou novamente no mesmo filme (não deve recarregar):\n")
    catalogo[0].mostrar_detalhes()
