from types import ModuleType

from step_counting.setup_recording import setup_recording, RecodingActivated
from profiler.profiler import create_profile, output_profile
from parser.parser import setup_parser
from utils import import_from_path, insert_module_to_path


def main() -> None:
    parser = setup_parser()
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_dir

    insert_module_to_path(input_file)

    eval_module: ModuleType = import_from_path(input_file)
    recorder, tracked_modules = setup_recording(eval_module, {'default_ib111'})

    with RecodingActivated():
        eval_module.testing_func()

    module_profiles = create_profile(tracked_modules, recorder.get_data())

    output_profile(module_profiles, output_file)

    evaluation = recorder.evaluate_data()
    print('SCORE:', evaluation)


if __name__ == '__main__':
    main()
