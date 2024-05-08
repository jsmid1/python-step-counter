# Stepcounter
Stepcounter is a performance measurement tool designed to assess the efficiency of Python code.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Testing](#testing)
- [Authors](#authors)

## Prerequisites
- Python 3.10 or higher
- pip version 22 or higher

## Installation
Clone this repository:

```bash
git clone https://github.com/jsmid1/python-step-counter.git
```

Move to the root folder of the project
(Replace "/path/to/clone" with the actual path):

```bash
cd /dir/with/clone/python-step-counter
```

Install the package:
```bash
pip install .
```

### Alternatives
For installation on a Linux system, you may install directly from PyPi:
```bash
pip install stepcounter
```

## Usage
After installation, you may use the tool with:
```bash
stepcounter /path/to/tested/file
```

### Configuration
The tool offers 3 modes of operation selectable with ```-m``` or ```--mode```:
- **DEFAULT** mode outputs only the score of a program.
- **SEQUENCE** mode gives information about the order of function calls.
- **DETAIL** mode outputs detailed profile of a program for each line.

If you wish to output to directory instead of stdout use ```-o``` or ```--output_dir```.

#### Example usage
```bash
stepcounter /path/to/tested/file -m=DETAIL -o=/path/to/output/dir
```


## Testing
To run all tests, execute this command in the root directory:
```bash
bash tests/test_run.sh
```
This script sets up the environment and runs all tests.

If you wish to run a specific test use
(Replace "/path/to/the/testfile" with the actual path):
```bash
python -m unittest /path/to/the/testfile        
```

## License
This project is licensed under the Apache License, Version 2.0 - see the [LICENSE](LICENSE) file for details.

## Authors
**Jan Šmíd** - [jsmid1](https://github.com/jsmid1)