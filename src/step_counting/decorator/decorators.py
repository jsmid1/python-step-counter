from types import ModuleType
import functools
from typing import Any, Callable, Optional, TypeAlias

from .records.record_classes import (
    SimpleCallRecorder,
    SequnceCallRecorder,
    DetailCallRecorder,
)
from .utils import (
    get_caller_module_info,
    get_method_type,
    module_in_list,
    determine_method,
)

Decorator: TypeAlias = Callable[
    [ModuleType, Optional[type], Callable[..., Any], str], Callable[..., Any]
]


def create_decorator_default(
    tracked_modules: set[ModuleType],
) -> tuple[Decorator, SimpleCallRecorder]:
    recorder = SimpleCallRecorder()

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
        def wrapper(*args: tuple[Any], **kwargs: tuple[Any]) -> Any:
            module, _ = get_caller_module_info()
            if module_in_list(module, tracked_modules):
                assert module
                recorder.add_record(
                    module, class_, determine_method(func_name, args), args
                )
            return func_obj(*args, **kwargs)

        if method_type in {classmethod, staticmethod}:
            return method_type(wrapper)
        return wrapper

    return decorator, recorder


def create_decorator_sequence(
    tracked_modules: set[ModuleType],
) -> tuple[Decorator, SequnceCallRecorder]:
    recorder = SequnceCallRecorder()

    def decorator(
        orig_module: ModuleType,
        class_: Optional[type],
        func: Callable[..., Any],
        func_name: str,
    ) -> Callable[..., Any]:
        method_type = get_method_type(orig_module, class_, func_name)
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
                    class_,
                    determine_method(func_name, args),
                )
            return func_obj(*args, **kwargs)

        if method_type in {classmethod, staticmethod}:
            return method_type(wrapper)  # type: ignore
        return wrapper

    return decorator, recorder


from ..utils.module import get_module_by_name


def create_decorator_detail(
    tracked_modules: set[ModuleType],
) -> tuple[Decorator, DetailCallRecorder]:
    recorder = DetailCallRecorder()

    def decorator(
        orig_module: ModuleType,
        class_: Optional[type],
        func: Callable[..., Any],
        func_name: str,
    ) -> Callable[..., Any]:
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
            return method_type(wrapper)  # type: ignore
        return wrapper

    return decorator, recorder
