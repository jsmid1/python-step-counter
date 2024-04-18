import os
from types import ModuleType
from typing import Any, Optional

from src.step_counting.decorator.records.record_classes import Counter


def create_module_profile(
    module_file: str, module_data: dict[int, dict[Any, Counter]]
) -> str:
    lines = []
    with open(module_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            lines.append(f'{line_number}: {line[0:-1]}')

            lines.append((90 - len(str(line_number)) - len(line)) * ' ')
            for record, counter in module_data.get(line_number, {}).items():
                module, class_, func = record
                lines.append(
                    f' # {module.__name__}.{class_.__name__ if class_ else None}.{func}: No of calls: {counter.get_count_total()}, Total eval: {counter.get_evaluation_total()}\n'
                )

                lines.append(91 * ' ')

            lines[-1] = '\n'

    return ''.join(lines)


def create_profile(
    modules: set[ModuleType],
    data: dict[
        ModuleType, dict[int, dict[tuple[ModuleType, Optional[type], str], Counter]]
    ],
) -> dict[ModuleType, str]:
    profiled_modules = dict()
    for module in modules:
        module_data = data.get(module, {})

        assert module.__file__
        profiled_modules[module] = create_module_profile(module.__file__, module_data)

    return profiled_modules


def output_to_stdout(module_profiles: dict[ModuleType, str]) -> None:
    for module, profile in module_profiles.items():
        print(module.__name__)
        print(profile)


def profile_to_file(profile: str, output_file: str) -> None:
    with open(output_file, 'w') as file:
        file.write(profile)


def output_to_dir(module_profiles: dict[ModuleType, str], output_dir: str) -> None:
    for module, profile in module_profiles.items():
        filepath = os.path.join(output_dir, module.__name__) + '.py'
        profile_to_file(profile, filepath)


def output_profile(module_profiles: dict[ModuleType, str], output_dir: str) -> None:
    if output_dir is None:
        output_to_stdout(module_profiles)
    else:
        output_to_dir(module_profiles, output_dir)
