import math


def constant(_):
    return 1


def logarithmic(args):
    n = args[0]
    return int(math.log(n, 2))


def linear(args):
    n = args[0]
    return int(n)


def linearithmic(args):
    n = args[0]
    # TODO remove float
    return int(float(n) * math.log(n))


def quadratic(args):
    n = args[0]
    return 5


def logarithmic_to_len(args):
    n = len(args[0])
    return logarithmic([n])


def linear_to_len(args):
    n = len(args[0])
    return linear([n])


def linearithmic_to_len(args):
    n = len(args[0])
    return linearithmic([n])


def quadratic_to_len(args):
    n = len(args[0])
    return quadratic([n])


def logarithmic_to_sec(args):
    n = args[1]
    return logarithmic([n])


def linear_to_sec(args):
    n = args[1]
    return linear([n])


def linearithmic_to_sec(args):
    n = args[1]
    return linearithmic([n])


def quadratic_to_sec(args):
    n = args[1]
    return quadratic([n])


def sequence_mul_complexity(args):
    sequence = args[0]
    multiplier = args[1]
    return multiplier * len(sequence)


def sequence_startswith_complexity(args):
    prefix = args[1]
    return len(prefix)


def sequence_join_complexity(args):
    separator = args[0]
    sequence_list = args[1]

    return sum(len(sequence) for sequence in sequence_list) + len(sequence_list) * len(
        separator
    )
