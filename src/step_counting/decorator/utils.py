import sys

dict_get = dict.get


def get_caller_module_info():
    try:
        caller_frame = sys._getframe(2)
    except:
        return None, 0

    module_name = dict_get(caller_frame.f_globals, '__name__', None)
    line_number = caller_frame.f_lineno

    return module_name, line_number
