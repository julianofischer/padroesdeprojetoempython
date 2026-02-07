"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# ruff: noqa: E402
# Exemplos de Strategy Pattern em Python
lista_de_frutas = ["maçã", "banana", "abacaxi", "laranja", "uva"]


def por_tamanho(fruta):
    return len(fruta)


def ordem_alfabetica(fruta):
    return fruta


lista_de_frutas.sort(key=por_tamanho)
print("Ordenado por tamanho:", lista_de_frutas)

lista_de_frutas.sort(key=ordem_alfabetica)
print("Ordenado alfabeticamente:", lista_de_frutas)

# lambdas
lista_de_frutas.sort(key=lambda fruta: len(fruta))
print("Ordenado por tamanho (lambda):", lista_de_frutas)

# dunder methods
# magic methods
# __hash__, __eq__, __lt__, __gt__, __le__, __ge__


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __lt__(self, other):
        return self.idade < other.idade  # Strategy: comparar por idade

    def __eq__(self, other):
        return self.nome == other.nome and self.idade == other.idade


p1 = Pessoa("Alice", 30)
p2 = Pessoa("Bob", 25)
print("Alice < Bob?", p1 < p2)  # Usa __lt__


# settings.py
# django permite configurar múltiplos backends de autenticação
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "django.contrib.auth.backends.RemoteUserBackend",
]


# No celery você troca facilmente como uma mensagem é serializada
CELERY_TASK_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "pickle"


# Template Method
# Django Forms usa Template Method para validação
from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith("@example.com"):
            raise forms.ValidationError("Email deve ser do domínio example.com")
        return email


# full_clean() chama hooks:
# entre eles, clean_<fieldname>()
def is_valid(self):
    self.cleaned_data = {}
    self._errors = {}
    self.full_clean()  # TEMPLATE METHOD
    return not self._errors


# unit tests
# Template Method
import unittest


class TestMinhaFuncionalidade(unittest.TestCase):
    def setUp(self):
        self.dados_teste = self.criar_dados_teste()

    def criar_dados_teste(self):
        # Strategy: trocar a forma de criar dados
        return {"nome": "Teste", "idade": 30}

    def test_algo(self):
        self.assertEqual(self.dados_teste["nome"], "Teste")


# Strategy resolve o problema quando cada regra é independente
# Mas e se as regras são semelhantes mas com pequenas variações?
# Nesse caso, o Template Method é mais adequado.
