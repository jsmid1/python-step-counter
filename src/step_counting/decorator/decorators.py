import functools

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


def create_decorator_default(tracked_modules):
    recorder = simple_call_recorder()

    def decorator(func, class_, func_name):
        method_type = get_method_type(class_, func_name)
        if method_type == classmethod:
            func_obj = func.__func__
        else:
            func_obj = func

        @functools.wraps(func_obj)
        def wrapper(*args, **kwargs):
            module, _ = get_caller_module_info()
            if module_in_list(module, tracked_modules):
                recorder.add_record(class_, determine_method(func_name, args), args)
            return func_obj(*args, **kwargs)

        if method_type in {classmethod, staticmethod}:
            return method_type(wrapper)
        return wrapper

    return decorator, recorder


def create_decorator_sequence(tracked_modules):
    recorder = sequence_call_recorder()

    def decorator(func, class_, func_name):
        method_type = get_method_type(class_, func_name)
        if method_type == classmethod:
            func_obj = func.__func__
        else:
            func_obj = func

        @functools.wraps(func_obj)
        def wrapper(*args, **kwargs):
            module, _ = get_caller_module_info()
            if module_in_list(module, tracked_modules):
                recorder.add_record(
                    module.__name__, class_, determine_method(func_name, args)
                )
            return func_obj(*args, **kwargs)

        if method_type in {classmethod, staticmethod}:
            return method_type(wrapper)
        return wrapper

    return decorator, recorder


def create_decorator_detail(tracked_modules):
    recorder = detail_call_recorder()

    def decorator(func, class_, func_name):
        method_type = get_method_type(class_, func_name)
        if method_type == classmethod:
            func_obj = func.__func__
        else:
            func_obj = func

        @functools.wraps(func_obj)
        def wrapper(*args, **kwargs):
            module, line_number = get_caller_module_info()
            if module_in_list(module, tracked_modules):
                assert module
                recorder.add_record(
                    module.__name__,
                    line_number,
                    class_,
                    determine_method(func_name, args),
                    args,
                )

            return func_obj(*args, **kwargs)

        if method_type in {classmethod, staticmethod}:
            return method_type(wrapper)
        return wrapper

    return decorator, recorder
