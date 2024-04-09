from typing import Any, Callable


def is_method(method: Callable[..., Any]) -> bool:
    return callable(method) or type(method) in {classmethod, staticmethod}


class MethodSwitch:
    def __init__(
        self: 'MethodSwitch',
        overwrite: Callable[..., Any],
        orig_method: Callable[..., Any],
        repl_method: Callable[..., Any],
    ) -> None:
        if not is_method(repl_method):
            raise Exception('Given replacement function is not callable')

        self.overwrite = overwrite
        self.__original_method = orig_method
        self.__replacement_method = repl_method

    def set_original_method(
        self: 'MethodSwitch', orig_method: Callable[..., Any]
    ) -> None:
        self.__original_method = orig_method

    def set_replacement_method(
        self: 'MethodSwitch', repl_method: Callable[..., Any]
    ) -> None:
        if not is_method(repl_method):
            raise Exception('Given replacement function is not callable')
        self.__replacement_method = repl_method

    def get_original_method(self: 'MethodSwitch') -> Callable[..., Any]:
        return self.__original_method

    def get_replacement_method(self: 'MethodSwitch') -> Callable[..., Any]:
        return self.__replacement_method
