"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# Padrão Proxy: fornece um substituto para outro objeto
# permitindo controlar o acesso a ele e/ou adicionar uma funcionalidade.
# # Exemplo: logging de acesso a configuração

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


class ConfigProxyLazyLoading:
    def __init__(self, arquivo="config.json"):
        self.arquivo = arquivo
        self._config = None

    def _carregar_config(self):
        if self._config is None:
            print("🔐 Carregando configuração...")
            self._config = Config(self.arquivo)

    @property
    def data(self):
        print("🔐 Acessando configuração...")
        self._carregar_config()
        return self._config.data

    # E se quiséssemos logar cada acesso a um atributo específico de data?
    class DataProxy:
        def __init__(self, config_proxy):
            self._config_proxy = config_proxy

        def __getitem__(self, chave):
            print(f"🔐 Acessando configuração para a chave: {chave}")
            return self._config_proxy.data.get(chave, None)

    @property
    def dados(self):
        return self.DataProxy(self)


def teste_config_proxy_logging():
    config = ConfigProxyLazyLoading()

    print("✅ Aplicação iniciada.")
    print("Tema configurado:", config.data["theme"])
    print("Idioma configurado:", config.data["language"])

    print("✅ Acessando configurações via DataProxy.")
    dados_proxy = config.dados
    dados_proxy["theme"]
    dados_proxy["language"]


if __name__ == "__main__":
    teste_config_proxy_logging()
