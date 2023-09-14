from abc import ABC, abstractmethod


class User:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


class UserRepositoryInterface(ABC):
    @abstractmethod
    def find_users_by_name(self):
        pass


class UserDB(UserRepositoryInterface):
    def find_users_by_name(self):
        with open('../db/database.csv', 'r') as user_file:
            return user_file.readline()


class UserFinder:
    def __init__(self, repository):
        self.repository = repository

    def find_user(self):
        return self.repository.find_users_by_name()


if __name__ == "__main__":
    repo = UserDB()
    user_finder = UserFinder(repo)
    user = user_finder.find_user()
    print(user)
