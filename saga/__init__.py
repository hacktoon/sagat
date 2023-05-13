import inspect
import functools
from typing import Any


class Response:
    def __init__(self, request: 'Request', value: Any) -> None:
        self.request = request
        self.value = value


class Request:
    '''
    - implements a service request lifecycle with special methods
    - store state of a service request
    - emits a Response object
    '''
    def __init__(self, service=None):
        self.service = service

    def __call__(self, *args, **kwargs):
        client_response = self.__call_run(*args, **kwargs)
        if self.is_valid(client_response):
            self.on_success(client_response)
        else:
            self.on_error(client_response)
        return client_response

    def __call__(self, *args, **kwargs):
        client_response = self.__call_run(*args, **kwargs)
        if self.is_valid(client_response):
            self.on_success(client_response)
        else:
            self.on_error(client_response)
        return client_response

    def __call_run(self, *args, **kwargs):
        try:
            return self.run(*args, **kwargs)
        except TypeError as e:
            print(e)
            return

    def run(self, *args, **kwargs):
        raise NotImplementedError

    def is_valid(self, result) -> bool:
        return bool(result)

    def on_success(self, result):
        return

    def on_error(self, result):
        return


class Service:
    '''
    Store state for a service, ex: session, header, client, etc
    - configuration
    - state
    '''

    def __init__(self, name: str) -> None:
        self.name = name
        for name, _Request in self.__annotations__.items():
            request = _Request(service=self)
            setattr(self, name, request)

######################################

class GetPokemon(Request):
    def run(self, name: str):
        return {'name': name}


class PokeAPI(Service):
    def get_pokemon(self, name: str):
        return GetPokemon(name)


svc = PokeAPI('etc')
print(svc.get_pokemon('ditto'))
svc.get_pokemon()


'''
saga
    1.  certificates = db.get_certificates(args)
    2.  domains = certificates.filter()
    ...

service
    pokeapi.get_pokemon()

'''