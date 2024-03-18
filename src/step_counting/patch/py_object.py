import ctypes

from ..non_builtin_types import (
    class_type,
    dict_items_type,
    dict_keys_type,
    dict_values_type,
    generator_type,
)


class PyObject(ctypes.Structure):
    pass


class PyTypeObject(ctypes.Structure):
    pass


# Data types
c_pyobject_p = ctypes.py_object
c_uint = ctypes.c_uint
c_uchar = ctypes.c_ubyte
c_int = ctypes.c_int
c_int32 = ctypes.c_int32
c_int64 = ctypes.c_int64
c_char_p = ctypes.c_char_p
c_void_p = ctypes.c_void_p
c_long = ctypes.c_long
c_ulong = ctypes.c_ulong

c_ssize_t = c_int64 if ctypes.sizeof(c_void_p) == 8 else c_int32

c_ptr = ctypes.POINTER
c_functype = ctypes.CFUNCTYPE


# Function types
unary = (c_pyobject_p, c_pyobject_p)
binary = (c_pyobject_p, c_pyobject_p, c_pyobject_p)
ternary = (c_pyobject_p, c_pyobject_p, c_pyobject_p, c_pyobject_p)
len_f = (c_ssize_t, c_pyobject_p)
index_f = (c_pyobject_p, c_pyobject_p, c_ssize_t)
iassign_f = (c_int, c_pyobject_p, c_ssize_t, c_pyobject_p)
init_f = (c_int, c_pyobject_p, c_pyobject_p, c_void_p)

int_ternary = (c_ssize_t, c_pyobject_p, c_pyobject_p, c_pyobject_p)

c_int_ternary = c_functype(*int_ternary)
c_unary = c_functype(*unary)
c_binary = c_functype(*binary)
c_ternary = c_functype(*ternary)
c_len_f = c_functype(*len_f)
c_index_f = c_functype(*index_f)
c_iassign_f = c_functype(*iassign_f)
c_init_f = c_functype(*init_f)

# Additional types for type object structure
c_destructor_type = c_functype(None, c_pyobject_p)
c_tp_richcompare_type = c_functype(c_pyobject_p, c_pyobject_p, c_pyobject_p, c_int)
c_setattro_type = c_functype(c_ssize_t, c_pyobject_p, c_pyobject_p, c_pyobject_p)
c_init_type = c_functype(c_ssize_t, c_pyobject_p, c_pyobject_p, c_pyobject_p)
c_tp_getattr_type = c_functype(c_pyobject_p, c_pyobject_p, c_char_p)
c_tp_setattr_type = c_functype(c_int, c_pyobject_p, c_char_p, c_pyobject_p)
c_tp_hash_type = c_functype(c_ssize_t, c_pyobject_p)
c_tp_clear_type = c_functype(c_ssize_t, c_pyobject_p)
c_tp_descr_set_type = c_functype(c_ssize_t, c_pyobject_p, c_pyobject_p, c_pyobject_p)
c_tp_alloc_type = c_functype(c_pyobject_p, c_pyobject_p, c_ssize_t)
c_tp_vectorcall = c_functype(
    c_pyobject_p, c_pyobject_p, c_pyobject_p, c_ssize_t, c_pyobject_p
)

c_visitproc = c_functype(c_ssize_t, c_pyobject_p, c_void_p)
c_tp_traverse_type = c_functype(c_ssize_t, c_pyobject_p, c_visitproc, c_void_p)

c_tp_new_type = c_functype(c_pyobject_p, PyTypeObject, c_pyobject_p, c_pyobject_p)

# Additional types for tp_as_number structure
c_nb_bool_type = c_functype(c_ssize_t, c_pyobject_p)

# Additional types for tp_as_sequence structure
c_sq_contains_type = c_functype(c_ssize_t, c_pyobject_p, c_pyobject_p)


class PyNumberMethods(ctypes.Structure):
    _fields_ = [
        ('nb_add', c_binary),
        ('nb_subtract', c_binary),
        ('nb_multiply', c_binary),
        ('nb_remainder', c_binary),
        ('nb_divmod', c_binary),
        ('nb_power', c_ternary),
        ('nb_negative', c_unary),
        ('nb_positive', c_unary),
        ('nb_absolute', c_unary),
        ('nb_bool', c_nb_bool_type),
        ('nb_invert', c_unary),
        ('nb_lshift', c_binary),
        ('nb_rshift', c_binary),
        ('nb_and', c_binary),
        ('nb_xor', c_binary),
        ('nb_or', c_binary),
        ('nb_int', c_unary),
        ('nb_reserved', c_void_p),
        ('nb_float', c_unary),
        ('nb_inplace_add', c_binary),
        ('nb_inplace_subtract', c_binary),
        ('nb_inplace_multiply', c_binary),
        ('nb_inplace_remainder', c_binary),
        ('nb_inplace_power', c_ternary),
        ('nb_inplace_lshift', c_binary),
        ('nb_inplace_rshift', c_binary),
        ('nb_inplace_and', c_binary),
        ('nb_inplace_xor', c_binary),
        ('nb_inplace_or', c_binary),
        ('nb_floor_divide', c_binary),
        ('nb_true_divide', c_binary),
        ('nb_inplace_floor_divide', c_binary),
        ('nb_inplace_true_divide', c_binary),
        ('nb_index', c_unary),
    ]


class PySequenceMethods(ctypes.Structure):
    _fields_ = [
        ('sq_length', c_len_f),
        ('sq_concat', c_binary),
        ('sq_repeat', c_index_f),
        ('sq_item', c_index_f),
        ('sq_slice', c_void_p),
        ('sq_ass_item', c_iassign_f),
        ('sq_ass_slice', c_void_p),
        ('sq_contains', c_sq_contains_type),
        ('sq_inplace_concat', c_binary),
        ('sq_inplace_repeat', c_index_f),
    ]


class PyMappingMethods(ctypes.Structure):
    _fields_ = [
        ('mp_length', c_len_f),
        ('mp_subscript', c_binary),
        ('mp_ass_subscript', c_int_ternary),
    ]


class PyAsyncMethods(ctypes.Structure):
    _fields_ = [
        ('am_await', c_unary),
        ('am_aiter', c_unary),
        ('am_anext', c_unary),
        # ('am_send', c_unary), # TODO: typedef PySendResult (*sendfunc)(PyObject *iter, PyObject *value, PyObject **result);
    ]


class PyBufferProcs(ctypes.Structure):
    _fields_ = [
        (
            'bf_getbuffer',
            c_unary,
        ),  # TODO: typedef int (*getbufferproc)(PyObject *, Py_buffer *, int);
        (
            'bf_releasebuffer',
            c_unary,
        ),  # TODO: typedef void (*releasebufferproc)(PyObject *, Py_buffer *); use ctypes.cbuffer
    ]


py_type_object_structs = {
    'tp_as_async': PyAsyncMethods,
    'tp_as_number': PyNumberMethods,
    'tp_as_sequence': PySequenceMethods,
    'tp_as_mapping': PyMappingMethods,
    'tp_as_buffer': PyBufferProcs,
}

method_mapping = {
    '__del__': ('tp_dealloc', None),
    '__repr__': ('tp_repr', None, unary),
    '__call__': ('tp_call', None),
    '__str__': ('tp_str', None, unary),
    '__getattribute__': ('tp_getattro', None),
    '__setattr__': ('tp_setattro', None),
    '__init__': (
        'tp_init',
        None,
        (c_ssize_t, c_pyobject_p, c_pyobject_p, c_pyobject_p),
    ),
    '__new__': (
        'tp_new',
        None,
        (c_pyobject_p, PyTypeObject, c_pyobject_p, c_pyobject_p),
    ),
    '__iter__': ('tp_iter', None, unary),
    '__next__': ('tp_iternext', None),
    # TODO decide how to handle this
    # probably one method for all comparisons to match the structure
    'comparison': (
        'tp_richcompare',
        None,
        (c_pyobject_p, c_pyobject_p, c_pyobject_p, c_int),
    ),  # to avoid confusion
    # '__eq__': ('tp_richcompare', None),
    # '__ne__': ('tp_richcompare', None),
    # '__lt__': ('tp_richcompare', None),
    # '__le__': ('tp_richcompare', None),
    # '__gt__': ('tp_richcompare', None),
    # '__ge__': ('tp_richcompare', None),
    '__hash__': ('tp_hash', None, (c_ssize_t, c_pyobject_p)),
    # # Finalize (typically for __del__, but Python's __del__ maps to tp_dealloc)
    # '__del__': ('tp_finalize', None),
    # Asynchronous execution methods mappings
    '__await__': ('tp_as_async', 'am_await'),
    '__aiter__': ('tp_as_async', 'am_aiter'),
    '__anext__': ('tp_as_async', 'am_anext'),
    # Numeric operations mappings
    '__sub__': ('tp_as_number', 'nb_subtract', binary),
    '__mod__': ('tp_as_number', 'nb_remainder', binary),
    '__divmod__': ('tp_as_number', 'nb_divmod', binary),
    '__pow__': ('tp_as_number', 'nb_power', ternary),
    '__neg__': ('tp_as_number', 'nb_negative', unary),
    '__pos__': ('tp_as_number', 'nb_positive', unary),
    '__abs__': ('tp_as_number', 'nb_absolute', unary),
    '__bool__': ('tp_as_number', 'nb_bool', (c_ssize_t, c_pyobject_p)),
    '__invert__': ('tp_as_number', 'nb_invert', unary),
    '__lshift__': ('tp_as_number', 'nb_lshift', binary),
    '__rshift__': ('tp_as_number', 'nb_rshift', binary),
    '__and__': ('tp_as_number', 'nb_and', binary),
    '__xor__': ('tp_as_number', 'nb_xor', binary),
    '__or__': ('tp_as_number', 'nb_or', binary),
    '__int__': ('tp_as_number', 'nb_int', unary),
    # nb_reserved
    '__float__': ('tp_as_number', 'nb_float', unary),
    '__iadd__': ('tp_as_number', 'nb_inplace_add', binary),
    '__isub__': ('tp_as_number', 'nb_inplace_subtract', binary),
    '__imul__': ('tp_as_number', 'nb_inplace_multiply', binary),
    '__imod__': ('tp_as_number', 'nb_inplace_remainder', binary),
    '__ipow__': ('tp_as_number', 'nb_inplace_power', ternary),
    '__ilshift__': ('tp_as_number', 'nb_inplace_lshift', binary),
    '__irshift__': ('tp_as_number', 'nb_inplace_rshift', binary),
    '__iand__': ('tp_as_number', 'nb_inplace_and', binary),
    '__ixor__': ('tp_as_number', 'nb_inplace_xor', binary),
    '__ior__': ('tp_as_number', 'nb_inplace_or', binary),
    '__truediv__': ('tp_as_number', 'nb_true_divide', binary),
    '__floordiv__': ('tp_as_number', 'nb_floor_divide', binary),
    '__itruediv__': ('tp_as_number', 'nb_inplace_true_divide', binary),
    '__ifloordiv__': ('tp_as_number', 'nb_inplace_floor_divide', binary),
    '__index__': ('tp_as_number', 'nb_index', unary),
    # Sequence operations mappings
    '__contains__': (
        'tp_as_sequence',
        'sq_contains',
        (c_ssize_t, c_pyobject_p, c_pyobject_p),
    ),
    '__rmul__': (
        'tp_as_sequence',
        'sq_repeat',
        (c_pyobject_p, c_pyobject_p, c_ssize_t),
    ),
    # Same as __mul__ for sequence types
    '__iadd__': ('tp_as_sequence', 'sq_inplace_concat', binary),
    '__imul__': (
        'tp_as_sequence',
        'sq_inplace_repeat',
        (c_pyobject_p, c_pyobject_p, c_ssize_t),
    ),
    # Deprecated in Python 3
    # '__setitem__': (
    #     'tp_as_sequence',
    #     'sq_ass_slice',
    #     'ssizessizeobjargproc',
    # ),
    '__delslice__': (
        'tp_as_sequence',
        'sq_ass_slice',
        'ssizessizeobjargproc',
    ),  # Deprecated in Python 3
    # Mapping operations mappings
    # '__delitem__': (
    #     'tp_as_mapping',
    #     'mp_ass_subscript',
    #     (c_ssize_t, c_pyobject_p, c_pyobject_p, c_pyobject_p),
    # ),
}

numeric_classes = [int, float, complex]
sequence_classes = [str, list, tuple, range]


def get_function_mapping(class_name, method_name):
    match method_name:
        case '__add__':
            if class_name in numeric_classes:
                return ('tp_as_number', 'nb_add', binary)
            return ('tp_as_sequence', 'sq_concat', binary)

        case '__mul__':
            if class_name in numeric_classes:
                return ('tp_as_number', 'nb_multiply', binary)
            return (
                'tp_as_sequence',
                'sq_repeat',
                (c_pyobject_p, c_pyobject_p, c_ssize_t),
            )

        case '__len__':
            if class_name in sequence_classes + [
                set,
                frozenset,
                dict_items_type,
                dict_keys_type,
                dict_values_type,
            ]:
                return ('tp_as_sequence', 'sq_length', (c_ssize_t, c_pyobject_p))
            return ('tp_as_mapping', 'mp_length', (c_ssize_t, c_pyobject_p))

        case '__getitem__':
            if class_name in sequence_classes + ['dict']:
                return (
                    'tp_as_sequence',
                    'sq_item',
                    (c_pyobject_p, c_pyobject_p, c_ssize_t),
                )
            return ('tp_as_mapping', 'mp_subscript', binary)

        case '__setitem__':
            if class_name in sequence_classes:
                return (
                    'tp_as_sequence',
                    'sq_ass_item',
                    iassign_f,
                )
            return (
                'tp_as_mapping',
                'mp_ass_subscript',
                (c_ssize_t, c_pyobject_p, c_pyobject_p, c_pyobject_p),
            )

        # deprecated in python3
        # case '__delitem__':
        #     if class_name in sequence_classes:
        #         return ('tp_as_sequence', 'sq_ass_item', (c_ssize_t, c_pyobject_p, c_pyobject_p, c_pyobject_p))
        #     return ('tp_as_mapping', 'mp_ass_subscript', (c_ssize_t, c_pyobject_p, c_pyobject_p, c_pyobject_p))

        case _:
            return method_mapping.get(method_name, None)


py_method_def_by_class = {
    str: [
        'encode',
        'replace',
        'split',
        'rsplit',
        'join',
        'capitalize',
        'casefold',
        'title',
        'center',
        'count',
        'expandtabs',
        'find',
        'partition',
        'index',
        'ljust',
        'lower',
        'lstrip',
        'rfind',
        'rindex',
        'rjust',
        'rstrip',
        'rpartition',
        'splitlines',
        'strip',
        'swapcase',
        'translate',
        'upper',
        'startswith',
        'endswith',
        'removeprefix',
        'removesuffix',
        'isascii',
        'islower',
        'isupper',
        'istitle',
        'isspace',
        'isdecimal',
        'isdigit',
        'isnumeric',
        'isalpha',
        'isalnum',
        'isidentifier',
        'isprintable',
        'zfill',
        'format',
        'format_map',
        '__format__',
        'maketrans',
        '__sizeof__',
        '__getnewargs__',
    ],
    list: [
        '__getitem__',
        '__reversed__',
        '__sizeof__',
        'clear',
        'copy',
        'append',
        'insert',
        'extend',
        'pop',
        'remove',
        'index',
        'count',
        'reverse',
        'sort',
        '__class_getitem__',
    ],
    dict: [
        '__sizeof__',
        'get',
        'setdefault',
        'pop',
        'popitem',
        'keys',
        'items',
        'values',
        'update',
        'fromkeys',
        'clear',
        'copy',
        '__reversed__',
        '__class_getitem__',
    ],
    set: [
        'add',
        'clear',
        '__contains__',
        'copy',
        'discard',
        'difference',
        'difference_update',
        'intersection',
        'intersection_update',
        'isdisjoint',
        'issubset',
        'issuperset',
        'pop',
        '__reduce__',
        'remove',
        '__sizeof__',
        'symmetric_difference',
        'symmetric_difference_update',
        'union',
        'update',
        '__class_getitem__',
    ],
    tuple: [
        '__getnewargs__',
        'index',
        'count',
        '__class_getitem__',
    ],
    int: [
        'conjugate',
        'bit_length',
        'bit_count',
        'to_bytes',
        'from_bytes',
        'as_integer_ratio',
        '__trunc__',
        '__floor__',
        '__ceil__',
        '__round__',
        '__getnewargs__',
        '__format__',
        '__sizeof__',
        #'is_integer',
    ],
    float: [
        'conjugate',
        '__trunc__',
        '__floor__',
        '__ceil__',
        '__round__',
        'as_integer_ratio',
        'fromhex',
        'hex',
        'is_integer',
        '__getnewargs__',
        '__getformat__',
        '__format__',
    ],
    bytes: [
        '__getnewargs__',
        'capitalize',
        'center',
        'count',
        'decode',
        'endswith',
        'expandtabs',
        'find',
        'fromhex',
        'hex',
        'index',
        'isalnum',
        'isalpha',
        'isascii',
        'isdigit',
        'islower',
        'isspace',
        'istitle',
        'isupper',
        'join',
        'ljust',
        'lower',
        'lstrip',
        'maketrans',
        'partition',
        'replace',
        'removeprefix',
        'removesuffix',
        'rfind',
        'rindex',
        'rjust',
        'rpartition',
        'rsplit',
        'rstrip',
        'split',
        'splitlines',
        'startswith',
        'strip',
        'swapcase',
        'title',
        'translate',
        'upper',
        'zfill',
    ],
    bytearray: [
        '__alloc__',
        # 'reduce',
        # 'reduce_ex',
        '__sizeof__',
        'append',
        'capitalize',
        'center',
        'clear',
        'copy',
        'count',
        'decode',
        'endswith',
        'expandtabs',
        'extend',
        'find',
        'fromhex',
        'hex',
        'index',
        'insert',
        'isalnum',
        'isalpha',
        'isascii',
        'isdigit',
        'islower',
        'isspace',
        'istitle',
        'isupper',
        'join',
        'ljust',
        'lower',
        'lstrip',
        'maketrans',
        'partition',
        'pop',
        'remove',
        'replace',
        'removeprefix',
        'removesuffix',
        'reverse',
        'rfind',
        'rindex',
        'rjust',
        'rpartition',
        'rsplit',
        'rstrip',
        'split',
        'splitlines',
        'startswith',
        'strip',
        'swapcase',
        'title',
        'translate',
        'upper',
        'zfill',
    ],
    complex: ['conjugate', 'imag', 'real'],
    range: [
        '__reversed__',
        '__reduce__',
        'count',
        'index',
    ],
    enumerate: ['__reduce__', '__class_getitem__'],
    generator_type: [
        'send',
        'throw',
        'close',
        '__sizeof__',
    ],
    dict_keys_type: [
        'isdisjoint',
        '__reversed__',
    ],
    dict_values_type: [
        '__reversed__',
    ],
    dict_items_type: [
        'isdisjoint',
        '__reversed__',
    ],
}

PyObject._fields_ = [
    ('ob_refcnt', c_ssize_t),
    ('ob_type', c_ptr(PyTypeObject)),
]

# TODO declare types
PyTypeObject._fields_ = [
    # varhead
    ('ob_base', PyObject),
    ('ob_size', c_ssize_t),
    # declaration
    ('tp_name', c_char_p),
    ('tp_basicsize', c_ssize_t),
    ('tp_itemsize', c_ssize_t),
    ('tp_dealloc', c_destructor_type),
    ('tp_vectorcall_offset', c_ssize_t),
    ('tp_getattr', c_tp_getattr_type),
    ('tp_setattr', c_tp_setattr_type),
    ('tp_as_async', c_ptr(PyAsyncMethods)),
    ('tp_repr', c_unary),
    ('tp_as_number', c_ptr(PyNumberMethods)),
    ('tp_as_sequence', c_ptr(PySequenceMethods)),
    ('tp_as_mapping', c_ptr(PyMappingMethods)),
    ('tp_hash', c_tp_hash_type),
    ('tp_call', c_ternary),
    ('tp_str', c_unary),
    ('tp_getattro', c_binary),
    ('tp_setattro', c_setattro_type),
    ('tp_as_buffer', c_ptr(PyBufferProcs)),
    ('tp_flags', c_ulong),
    ('tp_doc', c_char_p),
    ('tp_traverse', c_tp_traverse_type),
    ('tp_clear', c_tp_clear_type),
    ('tp_richcompare', c_tp_richcompare_type),
    ('tp_weaklistoffset', c_ssize_t),
    ('tp_iter', c_unary),
    ('tp_iternext', c_unary),
    ('tp_methods', c_void_p),  # Type not declared yet
    ('tp_members', c_void_p),  # Type not declared yet
    ('tp_getset', c_void_p),  # Type not declared yet
    ('tp_base', c_void_p),  # Type not declared yet
    ('tp_dict', c_pyobject_p),
    ('tp_descr_get', c_ternary),
    ('tp_descr_set', c_tp_descr_set_type),
    ('tp_dictoffset', c_ssize_t),
    ('tp_init', c_init_type),
    ('tp_alloc', c_tp_alloc_type),
    ('tp_new', c_tp_new_type),
    ('tp_free', c_destructor_type),
    ('tp_is_gc', c_destructor_type),
    ('tp_bases', c_pyobject_p),
    ('tp_mro', c_pyobject_p),
    ('tp_cache', c_pyobject_p),
    ('tp_subclasses', c_pyobject_p),
    ('tp_weaklist', c_pyobject_p),
    ('tp_del', c_destructor_type),
    ('tp_version_tag', c_uint),
    ('tp_finalize', c_destructor_type),
    ('tp_vectorcall', c_tp_vectorcall),
    ('tp_watched', c_uchar),
]
