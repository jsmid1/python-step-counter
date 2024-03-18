_callable = callable


class MethodSwitch:
    def __init__(
        self, overwrite, module, class_, method_name, orig_method, repl_method
    ):
        self.overwrite = overwrite
        self.module = module
        self.class_ = class_
        self.method_name = method_name
        self.__original_method = orig_method
        self.__replacement_method = repl_method

    def set_original_method(self, orig_method):
        if not _callable(orig_method):
            raise Exception('Given function is not callable')
        self.__original_method = orig_method

    def set_replacement_method(self, repl_method):
        if not _callable(repl_method):
            raise Exception('Given function is not callable')
        self.__replacement_method = repl_method

    def get_original_method(self):
        return self.__original_method

    def get_replacement_method(self):
        return self.__replacement_method
