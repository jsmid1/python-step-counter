#include <Python.h>
#include <stdio.h>

PyObject* dictionary_contains_patched_method;
PyObject* dictionary_len_patched_method;
PyObject* dictionary_delitem_patched_method;
PyObject* dictionary_getitem_patched_method;
PyObject* dictionary_setitem_patched_method;

static int patched_dictionary_contains(PyObject *self, PyObject* key) {
    PyObject* result = PyObject_CallFunction(dictionary_contains_patched_method, "(OO)", self, key);

    // TODO: Error checking
    return Py_IsTrue(result);
}

static long patched_dictionary_len(PyObject *self) {
    PyObject* result = PyObject_CallFunction(dictionary_len_patched_method, "(O)", self);

    return PyLong_AsLong(result);
}

// dict.__delitem__ internaly only calls dict.__setitem__ with value NULL. 
// Therefore it cannot be patched separately from dict.__setitem__.
// So to patch __delitem__ method we need to change setitem
// and change the behaviour in case value is NULL.
// static int patched_dictionary_delitem(PyObject *self, PyObject *key, PyObject* value) {
//     PyObject* result = PyObject_CallFunctionObjArgs(dictionary_delitem_patched_method, self, key, value);
//     //PyObject_CallFunction(dictionary_delitem_patched_method, "(OO)", self, key, NULL);

//         if (!result) {
//         // If result is NULL, an error occurred. You should set an appropriate error.
//         PyErr_SetString(PyExc_RuntimeError, "Error calling patched __setitem__ method");
//         return -1; // Indicate failure
//     }

//     Py_DECREF(result); // Clean up reference to result

//     return 0;
// }

static int patched_dictionary_setitem(PyObject *self, PyObject *key, PyObject *value) {
    PyObject* result = PyObject_CallFunction(dictionary_setitem_patched_method, "(OOO)", self, key, value);

        if (!result) {
        // If result is NULL, an error occurred. You should set an appropriate error.
        PyErr_SetString(PyExc_RuntimeError, "Error calling patched __setitem__ method");
        return -1; // Indicate failure
    }

    Py_DECREF(result); // Clean up reference to result

    return 0;
}

static PyObject *patched_dictionary_getitem(PyObject *self, PyObject* key) {
    PyObject* result = PyObject_CallFunction(dictionary_getitem_patched_method, "(OO)", self, key);

    return result;
}

static PyObject* patch_dictionary_len(PyObject* self, PyObject* args) {
    PyObject* patched_method;
    if (!PyArg_ParseTuple(args, "O", &patched_method)) {
        return NULL;
    }
    if (!PyCallable_Check(patched_method)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    Py_XINCREF(patched_method); // Increase reference count

    dictionary_len_patched_method = patched_method;

    PyTuple_Type.tp_as_sequence->sq_length = patched_dictionary_len;

    Py_RETURN_NONE;
}

static PyObject* patch_dictionary_contains(PyObject* self, PyObject* args) {
    PyObject* patched_method;
    if (!PyArg_ParseTuple(args, "O", &patched_method)) {
        return NULL;
    }

    if (!PyCallable_Check(patched_method)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    Py_XINCREF(patched_method); // Increase reference count

    dictionary_contains_patched_method = patched_method;

    PyDict_Type.tp_as_sequence->sq_contains = patched_dictionary_contains;

    Py_RETURN_NONE;
}

// static PyObject* patch_dictionary_delitem(PyObject* self, PyObject* args) {
//     PyObject* patched_method;
//     if (!PyArg_ParseTuple(args, "O", &patched_method)) {
//         return NULL;
//     }
//     if (!PyCallable_Check(patched_method)) {
//         PyErr_SetString(PyExc_TypeError, "parameter must be callable");
//         return NULL;
//     }

//     Py_XINCREF(patched_method); // Increase reference count

//     dictionary_delitem_patched_method = patched_method;

//     PyDict_Type.tp_as_mapping->mp_ass_subscript = patched_dictionary_delitem;

//     Py_RETURN_NONE;
// }

static PyObject* patch_dictionary_getitem(PyObject* self, PyObject* args) {
    PyObject* patched_method;
    if (!PyArg_ParseTuple(args, "O", &patched_method)) {
        return NULL;
    }
    if (!PyCallable_Check(patched_method)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    Py_XINCREF(patched_method); // Increase reference count

    dictionary_getitem_patched_method = patched_method;

    PyDict_Type.tp_as_mapping->mp_subscript = patched_dictionary_getitem;
    printf("\n\n\n\nXXXX\n\n\n");
    Py_RETURN_NONE;
}

static PyObject* patch_dictionary_setitem(PyObject* self, PyObject* args) {
    PyObject* patched_method;
    if (!PyArg_ParseTuple(args, "O", &patched_method)) {
        return NULL;
    }
    if (!PyCallable_Check(patched_method)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    Py_XINCREF(patched_method); // Increase reference count

    dictionary_setitem_patched_method = patched_method;

    PyDict_Type.tp_as_mapping->mp_ass_subscript = patched_dictionary_setitem;

    Py_RETURN_NONE;
}


PyObject* dict_iter_patched_method;

static PyObject* patched_dict_iter(PyObject *self) {
    PyObject* result = PyObject_CallFunction(dict_iter_patched_method, "(O)", self);

    // TODO: Error checking
    return result;
}


static PyObject* patch_dictionary_iter(PyObject* self, PyObject* args) {
    PyObject* patched_method;
    if (!PyArg_ParseTuple(args, "O", &patched_method)) {
        return NULL;
    }

    if (!PyCallable_Check(patched_method)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    Py_XINCREF(patched_method); // Increase reference count

    dict_iter_patched_method = patched_method;

    PyDict_Type.tp_iter = patched_dict_iter;

    Py_RETURN_NONE;
}


static PyMethodDef patchdictionary_methods[] = {
    {"patch_dictionary_contains", patch_dictionary_contains, METH_VARARGS, "Set the method for dictionary.__contains__ calls."},
    {"patch_dictionary_len", patch_dictionary_len, METH_VARARGS, "Set the method for dictionary.__len__ calls."},
    {"patch_dictionary_getitem", patch_dictionary_getitem, METH_VARARGS, "Set the method for dictionary.__getitem__ calls."},
    {"patch_dictionary_setitem", patch_dictionary_setitem, METH_VARARGS, "Set the method for dictionary.__setitem__ calls."},
    {"patch_dictionary_iter", patch_dictionary_iter, METH_VARARGS, "Set the method for dictionary.__oter__ calls."},
    {NULL, NULL, 0, NULL} // Sentinel, keep this for Python interpreter orientation
};


PyMODINIT_FUNC PyInit_patchdictionary(void) {
    static struct PyModuleDef modDef = {
        PyModuleDef_HEAD_INIT,
        "patchdictionary",
        "Module to patch dictionary methods",
        -1,
        patchdictionary_methods,
        NULL, NULL, NULL,
        NULL
    };

    PyObject *module = PyModule_Create(&modDef);
    if (!module) {
        return NULL;
    }

    return module;
}
