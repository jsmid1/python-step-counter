from ..complexities import ComplexitiesDict, constant, linear_to_len


tuple_complexities: ComplexitiesDict = {
    '__len__': constant,
    '__getitem__': constant,
    '__contains__': linear_to_len,
    '__iter__': constant,
    'count': linear_to_len,
    'index': linear_to_len,
}
