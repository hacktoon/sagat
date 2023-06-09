import logging

from saga import Service, Request, Response


class GetItem(Request):
    pass


class GetPokemon(Request):
    def run(self, name: str) -> Response:
        return {"name": name}

    def validate(self, value) -> bool:
        return len(value["name"]) > 3

    def success(self, value):
        logging.info(f"OK {value}")
        return value

    def error(self, value):
        logging.error(f"Error: {value}")
        return value


class PokeAPI(Service):
    #  method signatures are optional but useful for IDE autocompletion
    def get_pokemon(self, name: str) -> Response: ...
    def get_item(self, name: str) -> Response: ...


def test_request():
    pokeapi = PokeAPI()
    ditto = pokeapi.get_pokemon("ditto")
    assert ditto["name"] == "ditto"
