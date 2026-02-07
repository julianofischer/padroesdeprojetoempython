"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

from abc import ABC, abstractmethod


class Sender(ABC):
    @abstractmethod
    def send(self, msg: str) -> None:
        """Envia uma mensagem."""
        raise NotImplementedError


class EmailSender(Sender):
    def send(self, msg: str) -> None:
        print(f"[EMAIL] {msg}")


class SmsSender(Sender):
    def send(self, msg: str) -> None:
        print(f"[SMS] {msg}")


class WhatsAppSender:
    def send(self, msg: str) -> None:
        print(f"[WhatsApp] {msg}")


class UserNotifier:
    def __init__(self, sender: Sender):
        self.sender = sender

    def notify(self, user: str):
        self.sender.send(f"Olá, {user}!")


# Aplicação:
notifier = UserNotifier(EmailSender())
notifier.notify("Maria")

# Se quiser trocar a dependência:
notifier_sms = UserNotifier(SmsSender())
notifier_sms.notify("Carlos")

notifier_whats = UserNotifier(WhatsAppSender())
notifier_whats.notify("Juliano")
