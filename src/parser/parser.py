import argparse


def setup_parser():
    parser = argparse.ArgumentParser(description='Parse command line arguments')
    parser.add_argument('input_file', type=str, help='Input file')
    parser.add_argument(
        '-o', '--output_dir', type=str, help='Output directory', required=False
    )

    return parser
