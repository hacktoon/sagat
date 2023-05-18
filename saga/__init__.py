from typing import Any

from saga import Saga
from service import Service
from request import Request, Response


class GetPokemonRequest(Request):
    def run(self, name: str) -> Any:
        return {"name": f"{name}"}

    def is_valid(self, result) -> bool:
        return len(result["name"]) > 3

    def on_success(self, result):
        print(f"OK {result}")
        return result

    def on_error(self, result):
        print("Erro ", result)
        return result


class PokeAPI(Service):
    def get_pokemon(self, name: str) -> Response:
        return GetPokemonRequest.init(self, name)


class GetPokemonSaga(Saga):
    pokeapi = PokeAPI("Pokemon API")

    def run(self, name: str) -> Response:
        return self.pokeapi.get_pokemon(name)


saga = GetPokemonSaga()
saga.run('ditto')
