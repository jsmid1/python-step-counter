import ctypes

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

int_ternary = (c_int, c_pyobject_p, c_pyobject_p, c_pyobject_p)

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
