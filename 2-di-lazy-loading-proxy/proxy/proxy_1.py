"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# Evitar o acesso direto a um objeto, controlando sua criação e acesso
# Exemplo: controle de acesso, cache, logging, etc.
# E se eu quiser fazer lazy loading em um classe já implementada sem alterá-la?

import json
import os
import pathlib


class Config:
    THIS_DIR = pathlib.Path(__file__).parent

    def __init__(self, arquivo="config.json"):
        arquivo = os.path.join(self.THIS_DIR, arquivo)
        with open(arquivo) as f:
            print("📂 Lendo arquivo de configuração...")
            self.data = json.load(f)


class ConfigProxy:
    def __init__(self, arquivo="config.json"):
        self.arquivo = arquivo
        self._config = None

    def _carregar_config(self):
        if self._config is None:
            self._config = Config(self.arquivo)

    @property
    def data(self):
        self._carregar_config()
        return self._config.data


def teste_config_proxy():
    config = ConfigProxy()

    print("✅ Aplicação iniciada.")
    config.data["theme"]
    print("✅ Aplicação iniciada.")
    print("Tema configurado:", config.data["theme"])
    print("Idioma configurado:", config.data["language"])


if __name__ == "__main__":
    teste_config_proxy()
