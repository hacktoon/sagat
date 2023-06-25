from typing import Any, Callable


class Saga:
    def __init__(self, name: str, config: dict = None) -> None:
        self.name = name
        self.config = config

    def run(self, *args, **kwargs) -> "SagaResponse":
        return SagaResponse()


class SagaResponse:
    def __init__(self, value: Any = None) -> None:
        self.value = value


def service(ServiceClass):
    return ServiceClass


def request(_request: Callable) -> Callable:
    return _request