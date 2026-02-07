"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

import time
from pathlib import Path


class ArquivoReal:
    """
    Representa um arquivo de verdade, já carregado na memória.
    Ao ser criado, ele LÊ o conteúdo do disco imediatamente.
    """

    def __init__(self, caminho: str):
        self.caminho = Path(caminho)

        if not self.caminho.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {self.caminho}")

        # Simula uma operação lenta de leitura
        print(f"[ArquivoReal] Lendo arquivo do disco: {self.caminho}")
        time.sleep(1)  # simulação de custo

        # Lê todo o conteúdo em memória (binário)
        self._conteudo = self.caminho.read_bytes()

    def tamanho_em_bytes(self) -> int:
        """Retorna o tamanho do conteúdo em bytes."""
        return len(self._conteudo)

    def preview_texto(self, n: int = 100) -> str:
        """
        Tenta decodificar o conteúdo como texto (UTF-8) e
        retorna apenas os primeiros n caracteres para exibição.
        """
        try:
            texto_completo = self._conteudo.decode("utf-8", errors="replace")
        except Exception:
            texto_completo = ""

        return texto_completo[:n]

    def mostrar_info(self):
        """Mostra informações simples sobre o arquivo."""
        print(f"[ArquivoReal] Caminho: {self.caminho}")
        print(f"[ArquivoReal] Tamanho: {self.tamanho_em_bytes()} bytes")
        print(f"[ArquivoReal] Preview: {repr(self.preview_texto())}")


class ArquivoProxy:
    """
    Proxy para um arquivo pesado.
    Não lê o conteúdo do disco ao ser criado.
    Apenas guarda o caminho e carrega o ArquivoReal
    quando algum método que precisa do conteúdo é chamado.

    Este é um exemplo de:
    - Proxy
    - Inicialização Tardia (Lazy Initialization)
    """

    def __init__(self, caminho: str):
        self.caminho = Path(caminho)
        self._arquivo_real = None  # ainda não carregado

    def _carregar_arquivo_real(self):
        """
        Inicialização tardia:
        Cria o ArquivoReal apenas na primeira vez que for necessário.
        """
        if self._arquivo_real is None:
            print(
                f"[ArquivoProxy] Criando ArquivoReal sob demanda para: {self.caminho}"
            )
            self._arquivo_real = ArquivoReal(self.caminho)

    def tamanho_em_bytes(self) -> int:
        """Garante que o arquivo foi carregado e delega a chamada."""
        self._carregar_arquivo_real()
        return self._arquivo_real.tamanho_em_bytes()

    def preview_texto(self, n: int = 100) -> str:
        """Garante que o arquivo foi carregado e delega a chamada."""
        self._carregar_arquivo_real()
        return self._arquivo_real.preview_texto(n)

    def mostrar_info(self):
        """Mostra informações do arquivo, carregando-o apenas se necessário."""
        self._carregar_arquivo_real()
        self._arquivo_real.mostrar_info()


if __name__ == "__main__":
    # Exemplo de uso: imagine que você já tenha alguns arquivos de texto no diretório atual
    # Para testar, você pode criar arquivos simples, como:
    #
    # echo "exemplo de conteúdo 1" > arquivo1.txt
    # echo "outro conteúdo" > arquivo2.txt

    arquivos = [
        ArquivoProxy("arquivo1.txt"),
        ArquivoProxy("arquivo2.txt"),
    ]

    print("=== Lista de arquivos (apenas caminhos, sem leitura) ===")
    for arq in arquivos:
        print(f"- {arq.caminho}")
    print()

    print("=== Usuário pediu detalhes do primeiro arquivo ===")
    arquivos[0].mostrar_info()  # aqui o arquivo é realmente lido do disco
    print()

    print("=== Usuário pediu detalhes de novo do mesmo arquivo ===")
    arquivos[0].mostrar_info()  # aqui NÃO deve reler do disco, apenas reutilizar
    print()

    print("=== Usuário pediu detalhes do segundo arquivo ===")
    arquivos[1].mostrar_info()
