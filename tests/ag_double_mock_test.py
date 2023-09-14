"""
Tanto el espía como el mock en la terminología de Meszaros son objetos
que tienen memoria para registrar las llamadas que se les hacen.
Por otro lado, el stub no tiene memoria sino que simplemente devuelve los valores que le digamos.
Spy y mock se usan para validar salida indirecta,mientras que stub se utiliza para simular entrada indirecta.
La diferencia entre spy y el mock estricto es sutil porque ambos tienen memoria.
"""

from mamba import description, it
from expects import expect, equal
from src.af_double_spies import User, UserRepositoryInterface, UserService

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