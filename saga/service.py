import inspect
from typing import Optional

from .response import Response
from .request import Request


class Service:
    """
    Store state for a service, ex: session, header, client, etc
    Offer costly response cache
    - service configuration
    - service state
    - response cache
    """

    name: str = 'Service'

    def __init__(self, config: Optional[dict] = None) -> None:
        methods = inspect.getmembers(self, predicate=inspect.ismethod)
        for _method in methods:
            name, method = _method
            return_type = method.__annotations__.get('return')
            breakpoint()
        self.config = config
