from types import SimpleNamespace
from typing import Callable, ParamSpecArgs

from saga import Service, Request, Response




class GetItem(Request):
    pass


class GetPokemon(Request):
    def run(self, name: str) -> Response:
        return {"name": f"{name}"}

    def validate(self, value) -> bool:
        return len(value["name"]) > 3

    def success(self, value):
        print(f"OK {value}")
        return value

    def error(self, value):
        print("Erro ", value)
        return value


class PokeAPI(Service):
    name: str = 'PokeAPI'

    def get_pokemon(self, name: str) -> Response[GetPokemon]: ...
    def get_item(self, name: str) -> Response[GetItem]: ...


def test_request():
    pokeapi = PokeAPI()
    # breakpoint()
    resp = pokeapi.get_pokemon('ditto')
    assert resp.value == {"name": "ditto"}
