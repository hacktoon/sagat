import logging

from saga import Request, Response
from .model import Pokemon, Item


class GetItem(Request):
    def run(self, name: str) -> Item:
        return Item(name=name)


class GetPokemon(Request):
    def run(self, name: str) -> Pokemon:  # should be `Response`
        return Pokemon(name=name)

    def validate(self, value: Pokemon) -> bool:
        return len(value["name"]) > 3

    def success(self, value) -> Pokemon:
        logging.info(f"OK {value}")
        return Pokemon(name=value)

    def error(self, value) -> Pokemon:
        logging.error(f"Error: {value}")
        return Pokemon(name=None)

