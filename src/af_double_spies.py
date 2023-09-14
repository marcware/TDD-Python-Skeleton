"""
Los espías son objetos que tienen memoria para registrar
 las llamadas que se les hacen, las cuales podemos consultar
 para verificar si el artefacto que queremos probar tiene el comportamiento esperado.
Se usan, por tanto, para validar salidas indirectas.
"""
from abc import ABC, abstractmethod


class User:
    def __init__(self, name: str, surname: str, password: str):
        self._name = name
        self._surname = surname
        self._password = password

    def update_password(self, password: str):
        self._password = password

    def get_name(self):
        return self._name

    def get_password(self):
        return self._password


class UserRepositoryInterface(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        pass


class UserDB(UserRepositoryInterface):
    def save(self, user: User) -> None:
        with open('../db/database_spies.csv', 'w') as db:
            db.write(f"{user.get_name()};{user.get_password()}")


class UserService:
    def __init__(self, repository):
        self.repository = repository

    def update_password(self, user: User, password: str) -> User:
        user.update_password(password)
        self.repository.save(user)
        return user


if __name__ == "__main__":
    user = User("Pepe", "Martín", "old_pass123")
    repo = UserDB()
    user_finder = UserService(repo)
    user = user_finder.update_password(user, "new_pass123")
    print(f"{user.get_name()};{user.get_password()}")
