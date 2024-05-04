import math
from typing import Any, Callable, Dict, Hashable, Sequence, TypeAlias
from collections.abc import Sequence

ComplexitiesDict: TypeAlias = Dict[str, Callable[[tuple[Any, ...]], int]]


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
    return int(float.__mul__(float(n), math.log(n, 2)))


def quadratic(args: tuple[Any, ...]) -> int:
    n = args[0]
    return 5


def linear_to_bit_len(args: tuple[int, ...]) -> int:
    n = args[0]
    return n.bit_count()


def logarithmic_to_len(args: tuple[Any, ...]) -> int:
    n = len(args[0])
    return logarithmic((n,))


def logarithmic_to_min(args: tuple[int, int]) -> int:
    n1 = args[0]
    n2 = args[1]
    return logarithmic((min(n1, n2),))


def comparison_com(args: tuple[Any, ...]) -> int:
    s1 = args[0]
    s2 = args[1]

    total = 1
    if type(s1) != type(s2):
        return 1

    # Catch string to avoid creating substrings
    if isinstance(s1, str) and len(s1) == len(s2):
        return len(s1)

    if isinstance(s1, Sequence) and len(s1) == len(s2):
        for i in range(len(s1)):
            total += comparison_com((s1[i], s2[i]))

    if isinstance(s1, dict) and len(s1) == len(s2):
        for key in s1.keys():
            total += comparison_com((s1.get(key, None), s2.get(key, None)))

    return total


def hash_complexity(obj: Hashable) -> int:
    if isinstance(obj, (int, float)):
        return 1
    elif isinstance(obj, str):
        return len(obj)
    elif isinstance(obj, tuple):
        return sum(hash_complexity(item) for item in obj) + 1

    raise Exception(f"Unhashable type: {type(obj)}!")


def hash_complexity_sec(args: tuple[Any, ...]) -> int:
    obj = args[1]
    return hash_complexity(obj)


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


def linear_to_len_sec(args: tuple[Any, ...]) -> int:
    n = len(args[0])
    return linear((n,))


def linearithmic_to_sec(args: tuple[Any, int]) -> int:
    n = args[1]
    return linearithmic((n,))


def quadratic_to_sec(args: tuple[Any, int]) -> int:
    n = args[1]
    return quadratic((n,))


def linear_to_len_sum(args: tuple[Any, ...]) -> int:
    return sum([len(s) for s in args])


def sequence_mul_complexity(args: tuple[Sequence[Any], int]) -> int:
    sequence = args[0]
    multiplier = args[1]
    return multiplier * len(sequence)


def sequence_join_complexity(args: tuple[Any, ...]) -> int:
    separator = args[0]
    sequence_list = args[1]

    return sum(len(sequence) for sequence in sequence_list) + len(sequence_list) * len(
        separator
    )
