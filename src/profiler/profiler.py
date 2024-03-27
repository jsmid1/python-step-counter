import os


def create_module_profile(module_file, module_data):
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


def create_profile(modules, data):
    profiled_modules = dict()
    for module in modules:
        module_data = data.get(module.__name__, {})
        profiled_modules[module] = create_module_profile(module.__file__, module_data)

    return profiled_modules


def output_to_stdout(module_profiles):
    for module, profile in module_profiles.items():
        print(module.__name__)
        print(profile)


def profile_to_file(profile, output_file):
    with open(output_file, 'w') as file:
        file.write(profile)


def output_to_dir(module_profiles, output_dir):
    for module, profile in module_profiles.items():
        filepath = os.path.join(output_dir, module.__name__) + '.py'
        profile_to_file(profile, filepath)


def output_profile(module_profiles, output_dir):
    if output_dir is None:
        output_to_stdout(module_profiles)
    else:
        output_to_dir(module_profiles, output_dir)
