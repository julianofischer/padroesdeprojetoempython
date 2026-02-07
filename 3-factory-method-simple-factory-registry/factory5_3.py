"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# ruff: noqa: E402
from django.apps import apps

# Exemplo de uso, mas será ignorado através do try-except
# pois não temos o Django configurado aqui.

try:
    apps.get_model("auth", "User")  # retorna o modelo User dinamicamente
except:
    pass


from django.core.signals import request_finished
from django.dispatch import receiver


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")


from flask import Blueprint, Flask

bp = Blueprint("admin", __name__)
app = Flask(__name__)


@bp.route("/dashboard")
def dashboard():
    return "ok"


app.register_blueprint(bp)


import click


@click.group()
def cli():
    pass


@cli.command()
def build():
    print("building...")


@cli.command()
def deploy():
    print("deploying...")


# Mais em Pydantic, FastAPI, Typer, Celery, MatplotLib, Jinja2, SQLAlchemy, etc.
# Vantagens de usar o padrão Registry:
# - Desacopla o código cliente das classes concretas.
# - Facilita a adição de novas classes sem modificar o código existente.
# - Permite o registro dinâmico de classes em tempo de execução.
# - Pode ser combinado com decoradores para simplificar o registro de classes.

# Desvantangens ou pitfalls:
# - Pode dificultar o rastreamento de onde as classes são registradas.
# - Se não for bem documentado, pode confundir novos desenvolvedores.
# - Pode levar a problemas de namespace se não for gerenciado corretamente.
