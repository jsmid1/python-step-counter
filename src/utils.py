from types import ModuleType
import os
import sys
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec


def import_from_path(file_path: str) -> ModuleType:
    path = Path(file_path).resolve()
    module_name = path.stem

    spec = spec_from_file_location(module_name, str(path))
    if spec and spec.loader:
        module = module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
    else:
        raise ImportError(f'Could not load module from path: {file_path}')


def insert_module_to_path(input_file: str) -> None:
    module_dir = os.path.dirname(input_file)
    if module_dir not in sys.path:
        sys.path.insert(0, module_dir)
