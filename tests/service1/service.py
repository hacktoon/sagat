import saga
from .requests import GetPokemon, GetItem
from .model import Pokemon, Item


@saga.service
class PokeAPI:
    @saga.request(GetPokemon)
    def get_pokemon(self, name: str) -> Pokemon: ...

    @saga.request(GetItem)
    def get_item(self, name: str) -> Item: ...
