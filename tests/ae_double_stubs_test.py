"""
Estos stubs son el primer tipo de doble que vamos a ver. Son muy simples:
    no tienen memoria, sino que devuelven una respuesta concreta.
Se usan cuando la función que queremos probar no es directa, es decir,
que no solamente opera con los posibles argumentos que pueda tener sino que requiere de otra fuente de datos.
Los stubs permiten reemplazar esa fuente de datos.
"""

from mamba import description, it
from expects import expect, equal
from src.ae_double_stubs import UserRepositoryInterface, UserFinder

USER = "A_USER"

with description('The User Finder'):
    with it('searches user by name first'):
        class RepositoryStub(UserRepositoryInterface):
            def find_users_by_name(self):
                return USER


        user_repository = UserFinder(RepositoryStub())

        user = user_repository.find_user()

        expect(user).to(equal(USER))
