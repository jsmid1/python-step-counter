#include <Python.h>
#include <stdio.h>

PyObject* tuple_len_patched_method;
PyObject* tuple_getitem_patched_method;
PyObject* tuple_iterator_next_patched_method;


static PyObject * patched_tuple_iterator_next(PyObject *self) {
    printf("Calling tuple iternext\n\n");
    return PyObject_CallFunction(tuple_iterator_next_patched_method, "(O)", self);
}

static Py_ssize_t patched_tuple_len(PyObject *self) {
    PyObject* result = PyObject_CallFunction(tuple_len_patched_method, "(O)", self);

    return PyLong_AsLong(result);
}

static PyObject *patched_tuple_getitem(PyObject *self, PyObject * elem) {
    return PyObject_CallFunction(tuple_getitem_patched_method, "(OO)", self, elem);
}


static PyObject* patch_tuple_len(PyObject* self, PyObject* args) {
    PyObject* patched_method;
    if (!PyArg_ParseTuple(args, "O", &patched_method)) {
        return NULL;
    }
    if (!PyCallable_Check(patched_method)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    Py_XINCREF(patched_method); // Increase reference count

    tuple_len_patched_method = patched_method;
    
    PyTuple_Type.tp_as_sequence->sq_length = patched_tuple_len;

    Py_RETURN_NONE;
}

static PyObject* patch_tuple_getitem(PyObject* self, PyObject* args) {
    PyObject* patched_method;
    if (!PyArg_ParseTuple(args, "O", &patched_method)) {
        return NULL;
    }
    if (!PyCallable_Check(patched_method)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    Py_XINCREF(patched_method); // Increase reference count

    tuple_getitem_patched_method = patched_method;

    PyTuple_Type.tp_as_mapping->mp_subscript = patched_tuple_getitem;

    Py_RETURN_NONE;
}

static PyObject* patch_tuple_iterator_next(PyObject* self, PyObject* args) {
    PyObject* patched_method;
    if (!PyArg_ParseTuple(args, "O", &patched_method)) {
        return NULL;
    }
    if (!PyCallable_Check(patched_method)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    Py_XINCREF(patched_method); // Increase reference count

    tuple_iterator_next_patched_method = patched_method;

    PyTupleIter_Type.tp_iternext = patched_tuple_iterator_next;

    Py_RETURN_NONE;
}


static PyMethodDef patchtuple_methods[] = {
    {"patch_tuple_len", patch_tuple_len, METH_VARARGS, "Set the method for tuple.__len__ calls."},
    {"patch_tuple_getitem", patch_tuple_getitem, METH_VARARGS, "Set the method for tuple.__getitem__ calls."},
    {"patch_tuple_iterator_next", patch_tuple_iterator_next, METH_VARARGS, "Set the method for tuple_iterator.__next__ calls."},
    {NULL, NULL, 0, NULL} // Sentinel, keep this for Python interpreter orientation
};


PyMODINIT_FUNC PyInit_patchtuple(void) {
    static struct PyModuleDef modDef = {
        PyModuleDef_HEAD_INIT,
        "patchtuple",
        "Module to patch tuple methods",
        -1,
        patchtuple_methods, 
        NULL, NULL, NULL,
        NULL
    };

    PyObject *module = PyModule_Create(&modDef);
    if (!module) {
        return NULL;
    }

    return module;
}
