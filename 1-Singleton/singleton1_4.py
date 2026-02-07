"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

import json


# classe "privada"
class _Singleton:
    def __init__(self):
        print("Criando a instância única")


singleton = _Singleton()
dados = None

NOME_ARQUIVO = "config.json"
with open(NOME_ARQUIVO, "r") as f:
    dados = json.load(f)
