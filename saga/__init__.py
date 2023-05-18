import inspect
import functools
from typing import Any


class Response:
    def __init__(self, request: 'Request', value: Any) -> None:
        self.request = request
        self.value = value


class Request:
    service: 'Service'
    '''
    - implements a service request lifecycle with special methods
    - store state of a service request
    - emits a Response object
    '''

    @classmethod
    def send(cls, service, *args, **kwargs) -> Response:
        request = cls(service)
        value = request._run(*args, **kwargs)
        return Response(request, value)

    def __init__(self, service):
        self.service = service

    def _run(self, *args, **kwargs) -> Response:
        response = self._run_client(*args, **kwargs)
        if self.is_valid(response):
            self.on_success(response)
        else:
            self.on_error(response)
        return response

    def _run_client(self, *args, **kwargs):
        try:
            return self.run(*args, **kwargs)
        except TypeError as e:
            print(e)
            return

    def run(self, *args, **kwargs) -> Response:
        return

    def is_valid(self, result) -> bool:
        return bool(result)

    def on_success(self, result):
        return

    def on_error(self, result):
        return


class Service:
    '''
    Store state for a service, ex: session, header, client, etc
    Offer costly response cache
    - service configuration
    - service state
    - response cache
    '''

    def __init__(self, name: str, config: dict = None) -> None:
        self.name = name
        self.config = config

######################################

class GetPokemon(Request):
    def run(self, name: str) -> Response:
        return {'name': name}


class PokeAPI(Service):
    def get_pokemon(self, name: str) -> Response:
        # handle endpoint params here
        # maybe async / await
        return GetPokemon.send(self, name)


svc = PokeAPI('etc')
response = svc.get_pokemon('ditto')
print(response.value)


'''
saga
    1.  certificates = db.get_certificates(args)
    2.  domains = certificates.filter()
    ...

service
    pokeapi.get_pokemon()

'''