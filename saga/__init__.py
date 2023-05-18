from saga import Saga, SagaResponse
from service import Service
from request import Request, Response


######################################


class GetPokemon(Request):
    def run(self, name: str) -> Response:
        return {"name": name}


class PokeAPI(Service):
    def get_pokemon(self, name: str) -> Response:
        # handle endpoint params here
        # maybe async / await
        return GetPokemon.send(self, name)


class ServiceMap:
    pokeapi = PokeAPI("Pokemon API")


class PokeSaga(Saga):
    def run(self, name: str) -> 'SagaResponse':
        return self.pokeapi.get_pokemon(name)



pokesaga = PokeSaga()
print(pokesaga.run('ditto').value)
