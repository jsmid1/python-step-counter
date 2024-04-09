from typing import Any, Callable
from .complexities import constant

builtins_complexities: dict[str, Callable[[tuple[Any, ...]], int]] = {
    'ArithmeticError': constant,
    'AssertionError': constant,
    'AttributeError': constant,
    'BaseException': constant,
    'BlockingIOError': constant,
    'BrokenPipeError': constant,
    'BufferError': constant,
    'BytesWarning': constant,
    'ChildProcessError': constant,
    'ConnectionAbortedError': constant,
    'ConnectionError': constant,
    'ConnectionRefusedError': constant,
    'ConnectionResetError': constant,
    'DeprecationWarning': constant,
    'EOFError': constant,
    'Ellipsis': constant,
    'EncodingWarning': constant,
    'EnvironmentError': constant,
    'Exception': constant,
    'False': constant,
    'FileExistsError': constant,
    'FileNotFoundError': constant,
    'FloatingPointError': constant,
    'FutureWarning': constant,
    'GeneratorExit': constant,
    'IOError': constant,
    'ImportError': constant,
    'ImportWarning': constant,
    'IndentationError': constant,
    'IndexError': constant,
    'InterruptedError': constant,
    'IsADirectoryError': constant,
    'KeyError': constant,
    'KeyboardInterrupt': constant,
    'LookupError': constant,
    'MemoryError': constant,
    'ModuleNotFoundError': constant,
    'NameError': constant,
    'None': constant,
    'NotADirectoryError': constant,
    'NotImplemented': constant,
    'NotImplementedError': constant,
    'OSError': constant,
    'OverflowError': constant,
    'PendingDeprecationWarning': constant,
    'PermissionError': constant,
    'ProcessLookupError': constant,
    'RecursionError': constant,
    'ReferenceError': constant,
    'ResourceWarning': constant,
    'RuntimeError': constant,
    'RuntimeWarning': constant,
    'StopAsyncIteration': constant,
    'StopIteration': constant,
    'SyntaxError': constant,
    'SyntaxWarning': constant,
    'SystemError': constant,
    'SystemExit': constant,
    'TabError': constant,
    'TimeoutError': constant,
    'True': constant,
    'TypeError': constant,
    'UnboundLocalError': constant,
    'UnicodeDecodeError': constant,
    'UnicodeEncodeError': constant,
    'UnicodeError': constant,
    'UnicodeTranslateError': constant,
    'UnicodeWarning': constant,
    'UserWarning': constant,
    'ValueError': constant,
    'Warning': constant,
    'ZeroDivisionError': constant,
    '__build_class__': constant,
    '__debug__': constant,
    '__doc__': constant,
    '__import__': constant,
    '__loader__': constant,
    '__name__': constant,
    '__package__': constant,
    '__spec__': constant,
    'abs': constant,
    'aiter': constant,
    'all': constant,
    'anext': constant,
    'any': constant,
    'ascii': constant,
    'bin': constant,
    'bool': constant,
    'breakpoint': constant,
    'bytearray': constant,
    'bytes': constant,
    'callable': constant,
    'chr': constant,
    'classmethod': constant,
    'compile': constant,
    'complex': constant,
    'copyright': constant,
    'credits': constant,
    'delattr': constant,
    'dict': constant,
    'dir': constant,
    'divmod': constant,
    'enumerate': constant,
    'eval': constant,
    'exec': constant,
    'exit': constant,
    'filter': constant,
    'float': constant,
    'format': constant,
    'frozenset': constant,
    'getattr': constant,
    'globals': constant,
    'hasattr': constant,
    'hash': constant,
    'help': constant,
    'hex': constant,
    'id': constant,
    'input': constant,
    'int': constant,
    'isinstance': constant,
    'issubclass': constant,
    'iter': constant,
    'len': constant,
    'license': constant,
    'list': constant,
    'locals': constant,
    'map': constant,
    'max': constant,
    'memoryview': constant,
    'min': constant,
    'next': constant,
    'object': constant,
    'oct': constant,
    'open': constant,
    'ord': constant,
    'pow': constant,
    'print': constant,
    'property': constant,
    'quit': constant,
    'range': constant,
    'repr': constant,
    'reversed': constant,
    'round': constant,
    'set': constant,
    'setattr': constant,
    'slice': constant,
    'sorted': constant,
    'staticmethod': constant,
    'str': constant,
    'sum': constant,
    'super': constant,
    'tuple': constant,
    'type': constant,
    'vars': constant,
    'zip': constant,
}
