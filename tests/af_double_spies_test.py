"""
Los espías son objetos que tienen memoria para registrar
 las llamadas que se les hacen, las cuales podemos consultar
 para verificar si el artefacto que queremos probar tiene el comportamiento esperado.
Se usan, por tanto, para validar salidas indirectas.
"""

from mamba import description, it
from expects import expect, equal
from src.af_double_spies import User, UserRepositoryInterface, UserService

USER = "A_USER"

with description('The User Service'):
    with it('saves user throughout the repository'):
        class RepositorySpy(UserRepositoryInterface):
            save_user: USER = None

            def save(self, user: User) -> None:
                self.save_user = user


        repository = RepositorySpy()
        service = UserService(repository)
        user = User("Pepe", "Martín", "old_pass123")

        service.update_password(user, "new_pass123")

        expect(repository.save_user).to(equal(user))
