def is_method(method):
    return callable(method) or type(method) in {classmethod, staticmethod}


class MethodSwitch:
    def __init__(self, overwrite, orig_method, repl_method):
        if not is_method(repl_method):
            raise Exception('Given replacement function is not callable')

        self.overwrite = overwrite
        self.__original_method = orig_method
        self.__replacement_method = repl_method

    def set_original_method(self, orig_method):
        self.__original_method = orig_method

    def set_replacement_method(self, repl_method):
        if not is_method(repl_method):
            raise Exception('Given replacement function is not callable')
        self.__replacement_method = repl_method

    def get_original_method(self):
        return self.__original_method

    def get_replacement_method(self):
        return self.__replacement_method
