"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

from abc import ABC, abstractmethod
from typing import List


class BaseValidator(ABC):
    """
    Classe base que define o Template Method para validação.
    As subclasses implementam os passos específicos.
    """

    def validate(self, data: dict) -> List[str]:
        """
        Template Method: controla o fluxo da validação.
        Subclasses não devem sobrescrever esse método.
        """
        errors: List[str] = []

        self.check_required_fields(data, errors)
        self.check_formats(data, errors)
        self.check_business_rules(data, errors)

        return errors

    @abstractmethod
    def check_required_fields(self, data: dict, errors: List[str]) -> None:
        pass

    @abstractmethod
    def check_formats(self, data: dict, errors: List[str]) -> None:
        pass

    @abstractmethod
    def check_business_rules(self, data: dict, errors: List[str]) -> None:
        pass


class UserValidatorTM(BaseValidator):
    """
    Validador de usuário:
    - Campos obrigatórios: name, email, password
    - Formato: email deve conter "@"
    - Regra de negócio: senha com pelo menos 6 caracteres
    """

    def check_required_fields(self, data: dict, errors: List[str]) -> None:
        required = ["name", "email", "password"]
        for field in required:
            if field not in data or data[field] in (None, ""):
                errors.append(f"Campo obrigatório ausente ou vazio: {field}")

    def check_formats(self, data: dict, errors: List[str]) -> None:
        email = data.get("email")
        if email is not None and "@" not in email:
            errors.append("Email inválido: deve conter '@'.")

    def check_business_rules(self, data: dict, errors: List[str]) -> None:
        password = data.get("password", "")
        if len(password) < 6:
            errors.append("Senha deve ter pelo menos 6 caracteres.")


class AddressValidatorTM(BaseValidator):
    """
    Validador de endereço:
    - Campos obrigatórios: street, city, zip_code
    - Formato: zip_code com pelo menos 8 caracteres numéricos
    - Regra de negócio: city não pode ser 'teste'
    """

    def check_required_fields(self, data: dict, errors: List[str]) -> None:
        required = ["street", "city", "zip_code"]
        for field in required:
            if field not in data or data[field] in (None, ""):
                errors.append(f"Campo obrigatório ausente ou vazio: {field}")

    def check_formats(self, data: dict, errors: List[str]) -> None:
        zip_code = data.get("zip_code", "")
        if not (len(zip_code) >= 8 and zip_code.isdigit()):
            errors.append("zip_code inválido: deve ter pelo menos 8 dígitos numéricos.")

    def check_business_rules(self, data: dict, errors: List[str]) -> None:
        city = data.get("city", "")
        if city.lower() == "teste":
            errors.append("Cidade 'teste' não é permitida pelas regras de negócio.")


def main():
    user_valid = {
        "name": "Ana",
        "email": "ana@example.com",
        "password": "segura123",
    }

    user_invalid = {
        "name": "",
        "email": "anaexample.com",  # sem "@"
        "password": "123",  # curta
    }

    addr_valid = {
        "street": "Rua A",
        "city": "São Paulo",
        "zip_code": "12345678",
    }

    addr_invalid = {
        "street": "Rua B",
        "city": "teste",
        "zip_code": "12ab",
    }

    user_validator = UserValidatorTM()
    addr_validator = AddressValidatorTM()

    print("User válido - erros:", user_validator.validate(user_valid))
    print("User inválido - erros:", user_validator.validate(user_invalid))

    print("Address válido - erros:", addr_validator.validate(addr_valid))
    print("Address inválido - erros:", addr_validator.validate(addr_invalid))


if __name__ == "__main__":
    main()
