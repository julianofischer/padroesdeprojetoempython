"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

from typing import Protocol


class Sender(Protocol):
    def send(self, msg: str) -> None: ...


class EmailSender:
    def send(self, msg: str) -> None:
        print(f"[EMAIL] {msg}")


class SmsSender:
    def send(self, msg: str) -> None:
        print(f"[SMS] {msg}")


# inversão de controle
# separação de responsabilidades
class UserNotifier:
    def __init__(self, sender: Sender):
        self.sender = sender

    def notify(self, user: str):
        self.sender.send(f"Olá, {user}!")


# Aplicação:
notifier = UserNotifier(EmailSender())
notifier.notify("Maria")  # depois posso trocar para SmsSender()

notifier_sms = UserNotifier(SmsSender())
notifier_sms.notify("Juliano")
