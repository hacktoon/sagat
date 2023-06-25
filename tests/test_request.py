from .service1.service import PokeAPI


def test_request():
    pokeapi = PokeAPI()
    ditto = pokeapi.get_pokemon("ditto")
    assert ditto["name"] == "ditto"
