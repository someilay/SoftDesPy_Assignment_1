from typing import Callable
from typing_extensions import Annotated
from fastapi import Query


class Operator:
    def __init__(self, op: Callable, *args: str, **params_desc: str):
        super().__init__()
        self.desc = args[0] if len(args) > 0 else None
        self.__op = op
        self.__params_desc = params_desc
        self.__check_params()
        self.__handle_parameters()

    def __check_params(self):
        for param_name in self.__params_desc:
            if param_name not in self.__op.__annotations__:
                raise ValueError(f"{param_name} is not in args of provided operator")

    def __handle_parameters(self):
        for param_name, desc in self.__params_desc.items():
            param_type = self.__op.__annotations__[param_name]
            self.__op.__annotations__[param_name] = Annotated[param_type, Query(description=desc)]

    def get_endpoint(self) -> Callable:
        return self.__op


def make_operator(*args: str | Callable, **params_desc: str):
    if len(args) == 0 or isinstance(args[0], str):
        def wrapper(func: Callable):
            return Operator(func, *args, **params_desc)
        return wrapper
    return Operator(args[0])
