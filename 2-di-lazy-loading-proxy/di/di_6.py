"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

from fastapi import FastAPI, Depends

app = FastAPI()


class Logger:
    def log(self, msg: str):
        print(msg)


def get_logger() -> Logger:
    return Logger()


class UserService:
    def __init__(self, logger: Logger):
        self.logger = logger

    def create(self, name: str):
        self.logger.log(f"Criado: {name}")
        return {"name": name}


def get_user_service(logger: Logger = Depends(get_logger)):
    return UserService(logger)


@app.post("/users")
def create_user(name: str, service: UserService = Depends(get_user_service)):
    return service.create(name)
