"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

import json
from pprint import pprint


# Singleton: garantir que uma classe tenha apenas uma instância
# e fornecer um ponto global de acesso a ela.
class Singleton:
    NOME_DO_ARQUIVO = "config.json"
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Criando a instância única")
            cls._instancia = super().__new__(cls)
            with open(cls.NOME_DO_ARQUIVO, "r") as f:
                cls._instancia.dados = json.load(f)
        return cls._instancia


def main():
    s1 = Singleton()
    pprint(s1.dados)
    s2 = Singleton()
    print(s1 is s2)
    print(id(s1), id(s2))
    s3 = Singleton.__new__(Singleton)
    print(s1 is s3)


if __name__ == "__main__":
    main()
