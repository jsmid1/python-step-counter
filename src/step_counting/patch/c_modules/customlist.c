#include <Python.h>
#include <stdio.h>

PyObject* list_contains_patched_method;

static int patched_list_contains(PyObject *self, PyObject* elem) {
    PyObject* result = PyObject_CallFunction(list_contains_patched_method, "(OO)", self, elem);

    // TODO: Error checking
    return Py_IsTrue(result);
}

static PyObject* patch_list_contains(PyObject* self, PyObject* args) {
    PyObject* patched_method;
    if (!PyArg_ParseTuple(args, "O", &patched_method)) {
        return NULL;
    }

    if (!PyCallable_Check(patched_method)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    Py_XINCREF(patched_method); // Increase reference count

    list_contains_patched_method = patched_method;

    PyList_Type.tp_as_sequence->sq_contains = patched_list_contains;

    Py_RETURN_NONE;
}

PyObject* list_iter_patched_method;

static PyObject* patched_list_iter(PyObject *self) {
    PyObject* result = PyObject_CallFunction(list_iter_patched_method, "(O)", self);

    // TODO: Error checking
    return result;
}

static PyObject* patch_list_iter(PyObject* self, PyObject* args) {
    PyObject* patched_method;
    if (!PyArg_ParseTuple(args, "O", &patched_method)) {
        return NULL;
    }

    if (!PyCallable_Check(patched_method)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    Py_XINCREF(patched_method); // Increase reference count

    list_iter_patched_method = patched_method;

    PyList_Type.tp_iter = patched_list_iter;

    Py_RETURN_NONE;
}

static PyMethodDef patchlist_methods[] = {
    {"patch_list_contains", patch_list_contains, METH_VARARGS, "Set the method for list.__contains__ calls."},
    {"patch_list_iter", patch_list_iter, METH_VARARGS, "Set the method for list.__iter__ calls."},
    {NULL, NULL, 0, NULL} // Sentinel, keep this for Python interpreter orientation
};


PyMODINIT_FUNC PyInit_patchlist(void) {
    static struct PyModuleDef modDef = {
        PyModuleDef_HEAD_INIT,
        "patchlist",
        "Module to patch list methods",
        -1,
        patchlist_methods, 
        NULL, NULL, NULL,
        NULL
    };

    PyObject *module = PyModule_Create(&modDef);
    if (!module) {
        return NULL;
    }

    return module;
}
