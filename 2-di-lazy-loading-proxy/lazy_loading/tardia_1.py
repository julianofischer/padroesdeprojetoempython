"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

import json
import pathlib
import os


class Config:
    THIS_DIR = pathlib.Path(__file__).parent

    def __init__(self, arquivo="config.json"):
        arquivo = os.path.join(self.THIS_DIR, arquivo)
        print("📂 Lendo arquivo de configuração...")
        with open(arquivo) as f:
            self.data = json.load(f)


config = Config()  # arquivo é lido aqui, imediatamente

print("✅ Aplicação iniciada.")
print("Tema configurado:", config.data["theme"])
