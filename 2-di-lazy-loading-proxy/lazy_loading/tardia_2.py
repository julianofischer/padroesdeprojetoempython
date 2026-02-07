"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

import json
import os
import pathlib


class Config:
    THIS_DIR = pathlib.Path(__file__).parent

    def __init__(self, arquivo="config.json"):
        self.arquivo = os.path.join(self.THIS_DIR, arquivo)
        self._data = None

    @property
    def data(self):
        if self._data is None:
            print("📂 Lendo arquivo de configuração...")
            with open(self.arquivo) as f:
                self._data = json.load(f)
        return self._data


config = Config()  # arquivo só é lido quando data for acessado

print("✅ Aplicação iniciada.")
config.data["theme"]
print("Tema configurado:", config.data["theme"])
print("Tema configurado:", config.data["theme"])
