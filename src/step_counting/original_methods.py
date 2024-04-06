import builtins

from .non_builtin_types import (
    generator_type,
    dict_keys_type,
    dict_values_type,
    dict_items_type,
)

_import = builtins.__import__
_setattr = setattr
_getattr = getattr
_hasattr = hasattr
_isinstance = isinstance
_type = type
_callable = callable

list_append = list.append
list_getitem = list.__getitem__
dict_get = dict.get
dict_getitem = dict.__getitem__
dict_setitem = dict.__setitem__
tuple_getitem = tuple.__getitem__
dict_keys = dict.keys
dict_values = dict.values

str_encode = str.encode
str_replace = str.replace
str_split = str.split
str_rsplit = str.rsplit
str_join = str.join
str_capitalize = str.capitalize
str_casefold = str.casefold
str_title = str.title
str_center = str.center
str_count = str.count
str_expandtabs = str.expandtabs
str_find = str.find
str_partition = str.partition
str_index = str.index
str_ljust = str.ljust
str_lower = str.lower
str_lstrip = str.lstrip
str_rfind = str.rfind
str_rindex = str.rindex
str_rjust = str.rjust
str_rstrip = str.rstrip
str_rpartition = str.rpartition
str_splitlines = str.splitlines
str_strip = str.strip
str_swapcase = str.swapcase
str_translate = str.translate
str_upper = str.upper
str_startswith = str.startswith
str_endswith = str.endswith
str_removeprefix = str.removeprefix
str_removesuffix = str.removesuffix
str_isascii = str.isascii
str_islower = str.islower
str_isupper = str.isupper
str_istitle = str.istitle
str_isspace = str.isspace
str_isdecimal = str.isdecimal
str_isdigit = str.isdigit
str_isnumeric = str.isnumeric
str_isalpha = str.isalpha
str_isalnum = str.isalnum
str_isidentifier = str.isidentifier
str_isprintable = str.isprintable
str_zfill = str.zfill
str_format = str.format
str_format_map = str.format_map
str_format = str.__format__
str_maketrans = str.maketrans
str_sizeof = str.__sizeof__
str_getnewargs = str.__getnewargs__
list_getitem = list.__getitem__
list_reversed = list.__reversed__
list_sizeof = list.__sizeof__
list_clear = list.clear
list_copy = list.copy
list_append = list.append
list_insert = list.insert
list_extend = list.extend
list_pop = list.pop
list_remove = list.remove
list_index = list.index
list_count = list.count
list_reverse = list.reverse
list_sort = list.sort
list_iter = list.__iter__
list_class_getitem = list.__class_getitem__
dict_contains = dict.__contains__
dict_getitem = dict.__getitem__
dict_sizeof = dict.__sizeof__
dict_get = dict.get
dict_setdefault = dict.setdefault
dict_pop = dict.pop
dict_popitem = dict.popitem
dict_keys = dict.keys
dict_items = dict.items
dict_values = dict.values
dict_update = dict.update
dict_fromkeys = dict.fromkeys
dict_clear = dict.clear
dict_copy = dict.copy
dict_reversed = dict.__reversed__
dict_class_getitem = dict.__class_getitem__
set_add = set.add
set_clear = set.clear
set_contains = set.__contains__
set_copy = set.copy
set_discard = set.discard
set_difference = set.difference
set_difference_update = set.difference_update
set_intersection = set.intersection
set_intersection_update = set.intersection_update
set_isdisjoint = set.isdisjoint
set_issubset = set.issubset
set_issuperset = set.issuperset
set_pop = set.pop
set_reduce = set.__reduce__
set_remove = set.remove
set_sizeof = set.__sizeof__
set_symmetric_difference = set.symmetric_difference
set_symmetric_difference_update = set.symmetric_difference_update
set_union = set.union
set_update = set.update
set_class_getitem = set.__class_getitem__
tuple_getnewargs = tuple.__getnewargs__
tuple_index = tuple.index
tuple_count = tuple.count
tuple_class_getitem = tuple.__class_getitem__
int_conjugate = int.conjugate
int_bit_length = int.bit_length
int_bit_count = int.bit_count
int_to_bytes = int.to_bytes
int_from_bytes = int.from_bytes
int_as_integer_ratio = int.as_integer_ratio
int_trunc = int.__trunc__
int_floor = int.__floor__
int_ceil = int.__ceil__
int_round = int.__round__
int_getnewargs = int.__getnewargs__
int_format = int.__format__
int_sizeof = int.__sizeof__
int_eq = int.__eq__
int_add = int.__add__
float_conjugate = float.conjugate
float_trunc = float.__trunc__
float_floor = float.__floor__
float_ceil = float.__ceil__
float_round = float.__round__
float_as_integer_ratio = float.as_integer_ratio
float_fromhex = float.fromhex
float_hex = float.hex
float_is_integer = float.is_integer
float_getnewargs = float.__getnewargs__
float_getformat = float.__getformat__
float_format = float.__format__
bytes_getnewargs = bytes.__getnewargs__
bytes_capitalize = bytes.capitalize
bytes_center = bytes.center
bytes_count = bytes.count
bytes_decode = bytes.decode
bytes_endswith = bytes.endswith
bytes_expandtabs = bytes.expandtabs
bytes_find = bytes.find
bytes_fromhex = bytes.fromhex
bytes_hex = bytes.hex
bytes_index = bytes.index
bytes_isalnum = bytes.isalnum
bytes_isalpha = bytes.isalpha
bytes_isascii = bytes.isascii
bytes_isdigit = bytes.isdigit
bytes_islower = bytes.islower
bytes_isspace = bytes.isspace
bytes_istitle = bytes.istitle
bytes_isupper = bytes.isupper
bytes_join = bytes.join
bytes_ljust = bytes.ljust
bytes_lower = bytes.lower
bytes_lstrip = bytes.lstrip
bytes_maketrans = bytes.maketrans
bytes_partition = bytes.partition
bytes_replace = bytes.replace
bytes_removeprefix = bytes.removeprefix
bytes_removesuffix = bytes.removesuffix
bytes_rfind = bytes.rfind
bytes_rindex = bytes.rindex
bytes_rjust = bytes.rjust
bytes_rpartition = bytes.rpartition
bytes_rsplit = bytes.rsplit
bytes_rstrip = bytes.rstrip
bytes_split = bytes.split
bytes_splitlines = bytes.splitlines
bytes_startswith = bytes.startswith
bytes_strip = bytes.strip
bytes_swapcase = bytes.swapcase
bytes_title = bytes.title
bytes_translate = bytes.translate
bytes_upper = bytes.upper
bytes_zfill = bytes.zfill
bytearray_alloc = bytearray.__alloc__
bytearray_sizeof = bytearray.__sizeof__
bytearray_append = bytearray.append
bytearray_capitalize = bytearray.capitalize
bytearray_center = bytearray.center
bytearray_clear = bytearray.clear
bytearray_copy = bytearray.copy
bytearray_count = bytearray.count
bytearray_decode = bytearray.decode
bytearray_endswith = bytearray.endswith
bytearray_expandtabs = bytearray.expandtabs
bytearray_extend = bytearray.extend
bytearray_find = bytearray.find
bytearray_fromhex = bytearray.fromhex
bytearray_hex = bytearray.hex
bytearray_index = bytearray.index
bytearray_insert = bytearray.insert
bytearray_isalnum = bytearray.isalnum
bytearray_isalpha = bytearray.isalpha
bytearray_isascii = bytearray.isascii
bytearray_isdigit = bytearray.isdigit
bytearray_islower = bytearray.islower
bytearray_isspace = bytearray.isspace
bytearray_istitle = bytearray.istitle
bytearray_isupper = bytearray.isupper
bytearray_join = bytearray.join
bytearray_ljust = bytearray.ljust
bytearray_lower = bytearray.lower
bytearray_lstrip = bytearray.lstrip
bytearray_maketrans = bytearray.maketrans
bytearray_partition = bytearray.partition
bytearray_pop = bytearray.pop
bytearray_remove = bytearray.remove
bytearray_replace = bytearray.replace
bytearray_removeprefix = bytearray.removeprefix
bytearray_removesuffix = bytearray.removesuffix
bytearray_reverse = bytearray.reverse
bytearray_rfind = bytearray.rfind
bytearray_rindex = bytearray.rindex
bytearray_rjust = bytearray.rjust
bytearray_rpartition = bytearray.rpartition
bytearray_rsplit = bytearray.rsplit
bytearray_rstrip = bytearray.rstrip
bytearray_split = bytearray.split
bytearray_splitlines = bytearray.splitlines
bytearray_startswith = bytearray.startswith
bytearray_strip = bytearray.strip
bytearray_swapcase = bytearray.swapcase
bytearray_title = bytearray.title
bytearray_translate = bytearray.translate
bytearray_upper = bytearray.upper
bytearray_zfill = bytearray.zfill
complex_conjugate = complex.conjugate
complex_imag = complex.imag
complex_real = complex.real
range_reversed = range.__reversed__
range_reduce = range.__reduce__
range_count = range.count
range_index = range.index
enumerate_reduce = enumerate.__reduce__
enumerate_class_getitem = enumerate.__class_getitem__
generator_send = generator_type.send
generator_throw = generator_type.throw
generator_close = generator_type.close
generator_sizeof = generator_type.__sizeof__

d_keys_isdisjoint = dict_keys_type.isdisjoint
d_keys_reversed = dict_keys_type.__reversed__
d_values_reversed = dict_values_type.__reversed__
d_items_isdisjoint = dict_items_type.isdisjoint
d_items_reversed = dict_items_type.__reversed__
