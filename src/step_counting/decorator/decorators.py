import functools

from .records.record_classes import (
    simple_call_recorder,
    sequence_call_recorder,
    detail_call_recorder,
)
from .utils import get_caller_module_info, obj_in_list, determine_method


def create_decorator_default(tracked_modules):
    recorder = simple_call_recorder()

    def decorator(func, class_, func_name):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            module_name, _ = get_caller_module_info()
            if obj_in_list(module_name, tracked_modules):
                recorder.add_record(class_, determine_method(func_name, args), args)
            return func(*args, **kwargs)

        return wrapper

    return decorator, recorder


def create_decorator_sequence(tracked_modules):
    recorder = sequence_call_recorder()

    def decorator(func, class_, func_name):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            module_name, _ = get_caller_module_info()
            if obj_in_list(module_name, tracked_modules):
                recorder.add_record(
                    module_name, class_, determine_method(func_name, args)
                )
            return func(*args, **kwargs)

        return wrapper

    return decorator, recorder


def create_decorator_detail(tracked_modules):
    recorder = detail_call_recorder()

    def decorator(func, class_, func_name):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            module_name, line_number = get_caller_module_info()
            if obj_in_list(module_name, tracked_modules):
                recorder.add_record(
                    module_name,
                    line_number,
                    class_,
                    determine_method(func_name, args),
                    args,
                )

            return func(*args, **kwargs)

        return wrapper

    return decorator, recorder
