import argparse

from src.step_counting.setup_recording import setup_recording

import os
import importlib


def create_profile(module_file, module_data):
    lines = []
    with open(module_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            lines.append(f'{line_number}: {line[0:-1]}')

            lines.append((80 - len(str(line_number)) - len(line)) * ' ')
            for record, counter in module_data.get(line_number, {}).items():
                class_, func = record
                lines.append(
                    f' # {class_}.{func}: No of calls: {counter.get_count_total()}, Total eval: {counter.get_evaluation_total()}\n'
                )

                lines.append(81 * ' ')

            lines[-1] = '\n'

    return ''.join(lines)


def setup_parser():
    parser = argparse.ArgumentParser(description='Parse command line arguments')
    parser.add_argument('input_file', type=str, help='Input file')
    parser.add_argument('-d ')
    parser.add_argument('-o', '--output', type=str, help='Output file')

    return parser


import sys
from pathlib import Path


def import_from_path(file_path):
    path = Path(file_path).resolve()  # Ensure the path is absolute
    module_name = path.stem  # Use the file's stem as the module name

    spec = importlib.util.spec_from_file_location(module_name, str(path))
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
    else:
        raise ImportError(f'Could not load module from path: {file_path}')


def main():
    parser = setup_parser()
    args = parser.parse_args()

    input_file = args.input_file

    import sys

    module_dir = os.path.dirname(input_file)
    if module_dir not in sys.path:
        sys.path.insert(0, module_dir)

    eval_module = import_from_path(input_file)

    recorder, imports = setup_recording(eval_module)

    eval_module = import_from_path(input_file)
    recorder.clear_data()

    # eval_module = import_from_path(input_file)
    eval_module.testing_func()

    for import_ in imports:
        print(
            create_profile(
                import_.__file__, recorder.get_data().get(import_.__name__, {})
            )
        )

    print('SCORE:', recorder.evaluate_data())


if __name__ == '__main__':
    main()
