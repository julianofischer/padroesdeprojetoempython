"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# ruff: noqa: E402
# Decoradores por aí!
from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
def listar():
    return [{"id": 1, "nome": "Maria"}]


from flask import Flask

app = Flask(__name__)


@app.route("/home")
def home():
    return "Olá!"


import click


@click.group()
def cli():
    pass


@cli.command()
def build():
    print("Build iniciado")


from django.db.models.signals import post_save
from django.dispatch import receiver


class User:
    pass


@receiver(post_save, sender=User)
def criar_perfil(sender, instance, created, **kwargs): ...


from celery import shared_task


@shared_task
def enviar_email():
    print("Email enviado!")


from dataclasses import dataclass


@dataclass
class Usuario:
    nome: str
    idade: int


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def ano_nascimento(self):
        from datetime import datetime

        return datetime.now().year - self.idade


class Math:
    @staticmethod
    def dobro(x):
        return x * 2

    @classmethod
    def criar(cls):
        return cls()


from functools import lru_cache


@lru_cache(maxsize=32)
def multiplicar(a, b):
    print(f"Calculando {a} * {b}")
    return a * b


print(multiplicar(2, 3))
print(multiplicar(2, 3))
print(multiplicar(4, 5))
print(multiplicar(4, 5))
