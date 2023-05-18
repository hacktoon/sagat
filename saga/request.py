from typing import Any
from service import Service


class Response:
    def __init__(self, value: Any = None, request: "Request" = None) -> None:
        self.value = value
        self.request = request


class Request:
    """
    - implements a service request lifecycle with special methods
    - store state of a service request
    - emits a Response object
    """

    service: Service

    @classmethod
    def init(cls, service, *args, **kwargs) -> Response:
        request = cls(service)
        value = request._run(*args, **kwargs)
        return Response(request, value)

    def __init__(self, service):
        self.service = service

    # INTERNAL METHODS ===========================
    def _run(self, *args, **kwargs) -> Response:
        result = self._client_run(*args, **kwargs)
        if self._client_is_valid(result):
            result = self._client_on_success(result)
        else:
            result = self._client_on_error(result)
        return Response(self.service, result)

    def _client_run(self, *args, **kwargs) -> Any:
        try:
            return self.run(*args, **kwargs)
        except Exception as e:
            print(e)
            return

    def _client_is_valid(self, result) -> bool:
        try:
            return bool(self.is_valid(result))
        except Exception:
            return False

    def _client_on_success(self, result) -> Any:
        try:
            return self.on_success(result)
        except Exception as e:
            print(e)
            return

    def _client_on_error(self, result) -> Any:
        try:
            return self.on_error(result)
        except Exception as e:
            print(e)
            return

    # OVERRIDE METHODS ===========================
    def run(self, *args, **kwargs) -> Any:
        return None

    def is_valid(self, result) -> bool:
        return bool(result)

    def on_success(self, result) -> Any:
        return result

    def on_error(self, result) -> Any:
        return result
