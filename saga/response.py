from typing import Any, TypeVar, Generic


T = TypeVar("T")


class Response(Generic[T]):
    def __init__(self, status: bool = False, value: Any = None) -> None:
        self.status = status
        self.value = value