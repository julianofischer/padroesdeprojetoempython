"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

from dataclasses import dataclass
from typing import Protocol


@dataclass
class User:
    nome: str
    email: str
    telefone: str


class Sender(Protocol):
    def send(self, msg: str) -> None: ...


class EmailSender:
    def send(self, msg: str) -> None:
        print(f"[EMAIL] {msg}")


class SmsSender:
    def send(self, msg: str) -> None:
        print(f"[SMS] {msg}")


class UserNotifier:
    def __init__(self, sender: Sender):
        # composition by constructor
        self.sender = sender

    def notify(self, user: User):
        self.sender.send(f"Olá, {user.nome}!")


def main():
    # Composition Root
    sender = EmailSender()
    notifier = UserNotifier(sender)  # <- as dependências “nascem” aqui

    user = User(nome="Maria", email="maria@example.com", telefone="123456789")
    notifier.notify(user)


if __name__ == "__main__":
    main()
