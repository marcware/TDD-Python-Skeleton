from mamba import description, it
from src.ah_double_fake import User, UserRepositoryInterface, UserService

USER = "A_USER"

with description('The User Service'):
    with it('saves user throughout the repository'):
        class RepositoryMock(UserRepositoryInterface):
            save_user: USER = None
            called: int = 0

            def save(self, user: User) -> None:
                self.called += 1

            def verify(self):
                if self.called > 1:
                    raise "Save method was called more than once"


        repository = RepositoryMock()
        service = UserService(repository)
        user = User("Pepe", "Martín", "old_pass123")

        service.update_password(user, "new_pass123")

        repository.verify()