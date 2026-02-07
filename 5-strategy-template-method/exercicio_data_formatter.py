"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

import json
from abc import ABC, abstractmethod

# ==============================
#   ESTRATÉGIA ABSTRATA
# ==============================


class FormatterStrategy(ABC):
    @abstractmethod
    def format(self, dados: dict) -> str:
        """Recebe um dicionário e retorna uma string formatada."""
        pass


# ==============================
#   ESTRATÉGIAS CONCRETAS
# ==============================


class JSONFormatter(FormatterStrategy):
    def format(self, dados: dict) -> str:
        # ensure_ascii=False para exibir acentos corretamente
        return json.dumps(dados, ensure_ascii=False)


class CSVFormatter(FormatterStrategy):
    def format(self, dados: dict) -> str:
        # Cabeçalho: chaves do dicionário
        cabecalho = ",".join(dados.keys())
        # Linha de valores: valores do dicionário convertidos para string
        valores = ",".join(str(v) for v in dados.values())
        return f"{cabecalho}\n{valores}"


class YAMLFormatter(FormatterStrategy):
    def format(self, dados: dict) -> str:
        # Gera algo como:
        # nome: Ana
        # idade: 25
        linhas = []
        for chave, valor in dados.items():
            linhas.append(f"{chave}: {valor}")
        return "\n".join(linhas)


# ==============================
#   CONTEXTO
# ==============================


class DataFormatter:
    def __init__(self, strategy: FormatterStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: FormatterStrategy):
        """Permite trocar a estratégia em tempo de execução."""
        self._strategy = strategy

    def format(self, dados: dict) -> str:
        return self._strategy.format(dados)


# ==============================
#   CLIENTE
# ==============================


def escolher_estrategia(formato: str) -> FormatterStrategy:
    formato = formato.lower()
    if formato == "json":
        return JSONFormatter()
    elif formato == "csv":
        return CSVFormatter()
    elif formato == "yaml":
        return YAMLFormatter()
    else:
        raise ValueError(f"Formato não suportado: {formato}")


if __name__ == "__main__":
    dados = {"nome": "Ana", "idade": 25}

    print("=== Formatador de Dados (Strategy) ===")
    formato = input("Escolha o formato (json/csv/yaml): ")

    try:
        strategy = escolher_estrategia(formato)
    except ValueError as e:
        print("Erro:", e)
    else:
        formatter = DataFormatter(strategy)
        resultado = formatter.format(dados)
        print("\nResultado formatado:")
        print(resultado)
