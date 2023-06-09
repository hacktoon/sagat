from typing import Any

from .response import Response


class Request:
    """
    - implements a service request lifecycle with special methods
    - emits a Response object
    """

    ######################################################################
    # PUBLIC METHODS (override)
    ######################################################################
    def run(self, *args, **kwargs) -> Response:
        return Response(True, None)

    def is_valid(self, result) -> bool:
        return bool(result)

    def on_success(self, result) -> Response | None:
        return Response(True, None)

    def on_error(self, result) -> Response | None:
        return Response(False, None)

    ######################################################################
    # INTERNAL METHODS
    ######################################################################
    def __call__(self, *args, **kwargs) -> Response:
        raw_result = self.__run(*args, **kwargs)
        status = False
        if self.__is_valid(raw_result):
            result = self.__on_success(raw_result)
            status = True
        else:
            result = self.__on_error(raw_result)
        result = result if result is not None else raw_result
        return Response(status, result)

    def __run(self, *args, **kwargs) -> Any:
        try:
            return self.run(*args, **kwargs)
        except Exception as e:
            print(e)
            return

    def __is_valid(self, result) -> bool:
        try:
            return bool(self.is_valid(result))
        except Exception:
            return False

    def __on_success(self, result) -> Any:
        try:
            return self.on_success(result)
        except Exception as e:
            print(e)
            return

    def __on_error(self, result) -> Any:
        try:
            return self.on_error(result)
        except Exception as e:
            print(e)
            return
