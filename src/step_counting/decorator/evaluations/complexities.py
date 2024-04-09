import math
from typing import Any, Literal, Sequence


def constant(_: tuple[Any, ...]) -> int:
    return 1


def logarithmic(args: tuple[int]) -> int:
    n = args[0]
    return int(math.log(n, 2))


def linear(args: tuple[Any, ...]) -> int:
    n = args[0]
    return int(n)


def linearithmic(args: tuple[Any, ...]) -> int:
    n = args[0]
    return int(float.__mul__(float(n), math.log(n)))


def quadratic(args: tuple[Any, ...]) -> int:
    n = args[0]
    return 5


def logarithmic_to_len(args: tuple[Any, ...]) -> int:
    n = len(args[0])
    return logarithmic((n,))


def linear_to_len(args: tuple[Any, ...]) -> int:
    n = len(args[0])
    return linear((n,))


def linearithmic_to_len(args: tuple[Sequence[Any], ...]) -> int:
    n = len(args[0])
    return linearithmic((n,))


def quadratic_to_len(args: tuple[Any, int]) -> int:
    n = len(args[0])
    return quadratic((n,))


def logarithmic_to_sec(args: tuple[Any, int]) -> int:
    n = args[1]
    return logarithmic((n,))


def linear_to_sec(args: tuple[Any, int]) -> int:
    n = args[1]
    return linear((n,))


def linearithmic_to_sec(args: tuple[Any, int]) -> int:
    n = args[1]
    return linearithmic((n,))


def quadratic_to_sec(args: tuple[Any, int]) -> int:
    n = args[1]
    return quadratic((n,))


def sequence_mul_complexity(args: tuple[Sequence[Any], int]) -> int:
    sequence = args[0]
    multiplier = args[1]
    return multiplier * len(sequence)


def sequence_startswith_complexity(args: tuple[Any, ...]) -> int:
    prefix = args[1]
    return len(prefix)


def sequence_join_complexity(args: tuple[Any, ...]) -> int:
    separator = args[0]
    sequence_list = args[1]

    return sum(len(sequence) for sequence in sequence_list) + len(sequence_list) * len(
        separator
    )
