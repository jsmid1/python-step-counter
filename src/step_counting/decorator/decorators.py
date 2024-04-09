from types import FunctionType, ModuleType
import functools
from typing import Any, Callable, Optional

from .records.record_classes import (
    simple_call_recorder,
    sequence_call_recorder,
    detail_call_recorder,
)
from .utils import (
    get_caller_module_info,
    get_method_type,
    module_in_list,
    determine_method,
)


def create_decorator_default(
    tracked_modules: set[ModuleType],
) -> tuple[Callable[..., Any], simple_call_recorder]:
    recorder = simple_call_recorder()

    def decorator(
        orig_module: ModuleType,
        class_: Optional[type],
        func: Callable[..., Any],
        func_name: str,
    ) -> Any:
        method_type = get_method_type(class_, func_name)
        if method_type == classmethod:
            assert hasattr(func, '__func__')
            func_obj = func.__func__
        else:
            func_obj = func

        @functools.wraps(func_obj)
        def wrapper(*args: tuple[Any], **kwargs: tuple[Any]) -> Any:
            module, _ = get_caller_module_info()
            if module_in_list(module, tracked_modules):
                recorder.add_record(class_, determine_method(func_name, args), args)
            return func_obj(*args, **kwargs)

        if method_type in {classmethod, staticmethod}:
            return method_type(wrapper)
        return wrapper

    return decorator, recorder


def create_decorator_sequence(
    tracked_modules: set[ModuleType],
) -> tuple[
    Callable[[Any, Any, Any], Callable[[Any, Any], Any]], sequence_call_recorder
]:
    recorder = sequence_call_recorder()

    def decorator(
        orig_module: ModuleType,
        class_: Optional[type],
        func: Callable[..., Any],
        func_name: str,
    ) -> Any:
        method_type = get_method_type(class_, func_name)
        if method_type == classmethod:
            assert hasattr(func, '__func__')
            func_obj = func.__func__
        else:
            func_obj = func

        @functools.wraps(func_obj)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            module, _ = get_caller_module_info()
            if module_in_list(module, tracked_modules):
                assert module
                recorder.add_record(
                    orig_module,
                    module,
                    class_.__name__,
                    determine_method(func_name, args),
                )
            return func_obj(*args, **kwargs)

        if method_type in {classmethod, staticmethod}:
            return method_type(wrapper)
        return wrapper

    return decorator, recorder


def create_decorator_detail(
    tracked_modules: set[ModuleType],
) -> tuple[Callable[[Any, Any, Any], Callable[..., Any]], detail_call_recorder]:
    recorder = detail_call_recorder()

    def decorator(
        orig_module: ModuleType,
        class_: Optional[type],
        func: Callable[..., Any],
        func_name: str,
    ) -> Any:
        method_type = get_method_type(orig_module, class_, func_name)
        if method_type == classmethod:
            assert hasattr(func, '__func__')
            func_obj = func.__func__
        else:
            func_obj = func

        @functools.wraps(func_obj)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            module, line_number = get_caller_module_info()
            if module_in_list(module, tracked_modules):
                assert module
                recorder.add_record(
                    module,
                    line_number,
                    orig_module,
                    class_,
                    determine_method(func_name, args),
                    args,
                )

            return func_obj(*args, **kwargs)

        if method_type in {classmethod, staticmethod}:
            return method_type(wrapper)
        return wrapper

    return decorator, recorder
