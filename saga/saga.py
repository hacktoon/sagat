from typing import Any


class Saga:
    def __init__(self, name: str, config: dict = None) -> None:
        self.name = name
        self.config = config

    def run(self, *args, **kwargs) -> "SagaResponse":
        return SagaResponse()


class SagaResponse:
    def __init__(self, value: Any = None) -> None:
        self.value = value
