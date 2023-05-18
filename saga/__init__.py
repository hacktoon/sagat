import inspect
import functools
from typing import Any


class Response:
    def __init__(self, request: "Request" = None, value: Any = None) -> None:
        self.request = request
        self.value = value


class Request:
    service: "Service"
    """
    - implements a service request lifecycle with special methods
    - store state of a service request
    - emits a Response object
    """

    @classmethod
    def send(cls, service, *args, **kwargs) -> Response:
        request = cls(service)
        value = request._run(*args, **kwargs)
        return Response(request, value)

    def __init__(self, service):
        self.service = service

    def _run(self, *args, **kwargs) -> Response:
        response = self._client_run(*args, **kwargs)
        if self._client_is_valid(response):
            self._client_on_success(response)
        else:
            self.on_error(response)
        return response

    def _client_run(self, *args, **kwargs):
        try:
            return self.run(*args, **kwargs)
        except Exception as e:
            print(e)
            return

    def _client_is_valid(self, result) -> bool:
        try:
            return bool(self.is_valid(result))
        except Exception as e:
            return False

    def _client_on_success(self, result):
        try:
            return self.on_success(result)
        except Exception as e:
            print(e)
            return

    def _client_on_error(self, result):
        try:
            return self.on_error(result)
        except Exception as e:
            print(e)
            return

    def run(self, *args, **kwargs) -> Response:
        return Response()

    def is_valid(self, result) -> bool:
        return bool(result)

    def on_success(self, result):
        return result

    def on_error(self, result):
        return result


class Service:
    """
    Store state for a service, ex: session, header, client, etc
    Offer costly response cache
    - service configuration
    - service state
    - response cache
    """

    def __init__(self, name: str, config: dict = None) -> None:
        self.name = name
        self.config = config


######################################


class GetPokemon(Request):
    def run(self, name: str) -> Response:
        return {"name": name}


class PokeAPI(Service):
    def get_pokemon(self, name: str) -> Response:
        # handle endpoint params here
        # maybe async / await
        return GetPokemon.send(self, name)


svc = PokeAPI("etc")
response = svc.get_pokemon("ditto")
print(response.value)


"""
saga
    1.  certificates = db.get_certificates(args)
    2.  domains = certificates.filter()
    ...

service
    pokeapi.get_pokemon()

"""
