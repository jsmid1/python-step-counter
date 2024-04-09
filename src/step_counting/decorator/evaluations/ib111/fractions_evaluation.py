from ..complexities import constant, linear


fractions_complexities = {None}

fractions_fraction_complexities = {
    'as_integer_ratio': constant,
    'conjugate': constant,
    'denominator': constant,
    'from_decimal': constant,
    'from_float': constant,
    'imag': constant,
    'limit_denominator': constant,
    'numerator': constant,
    'real': constant,
}
