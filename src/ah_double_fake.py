from abc import ABC, abstractmethod


class User:
    def __init__(self, name: str, surname: str, password: str):
        self._name = name
        self._surname = surname
        self._password = password

    def update_password(self, password: str):
        self._password = password

    def update_name(self, name: str):
        self._name = name

    def is_equals(self, user:User):
        return self._name == user.get_name


    def get_name(self):
        return self._name

    def get_password(self):
        return self._password


class UserRepositoryInterface(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def add(self, user: User) -> None:
        pass

    @abstractmethod
    def delete(self, user: User) -> None:
        pass

    @abstractmethod
    def find_user_by(self, name: str) -> None:
        pass


class UserDB(UserRepositoryInterface):
    def add(self, user: User) -> None:
        pass

    def delete(self, user: User) -> None:
        pass

    def find_user_by(self, name: str) -> None:
        pass

    def save(self, user: User) -> None:
        with open('../db/database_spies.csv', 'w') as db:
            db.write(f"{user.get_name()};{user.get_password()}")


class UserService:
    def __init__(self, repository: UserRepositoryInterface):
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
