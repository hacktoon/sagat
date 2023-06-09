import inspect
import typing
from typing import Any, Optional

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
        self.endpoints = self.__build_endpoints()
        self.config = config

    def __build_endpoints(self):
        endpoints = {}
        methods = inspect.getmembers(self, predicate=inspect.ismethod)
        for name, method in methods:
            return_type = inspect.signature(method).return_annotation
            response = typing.get_origin(return_type)
            requests = typing.get_args(return_type)
            if response and requests and len(requests):
                # add/map the Request instance
                endpoints[name] = requests[0]()
        return endpoints

    def __getattribute__(self, name: str) -> Any:
        attr = super().__getattribute__(name)
        if 'endpoints' in super().__getattribute__('__dict__'):
            endpoints = super().__getattribute__('endpoints')
            if name in endpoints:
                # return the request object added via type hint
                return endpoints[name]
        return attr
