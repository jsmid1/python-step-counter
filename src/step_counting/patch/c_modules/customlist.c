#include <Python.h>
#include <stdio.h>

PyObject* list_contains_patched_method;
PyObject* list_iter_patched_method;
PyObject* list_getitem_patched_method;
PyObject* list_setitem_patched_method;

static objobjargproc original_list_setitem = NULL;

static int patched_list_contains(PyObject *self, PyObject* elem) {
    PyObject* result = PyObject_CallFunction(list_contains_patched_method, "(OO)", self, elem);

    return Py_IsTrue(result);
}

static PyObject* patched_list_iter(PyObject *self) {
    return PyObject_CallFunction(list_iter_patched_method, "(O)", self);
}

static PyObject *patched_list_getitem(PyObject *self, PyObject * elem) {
    return PyObject_CallFunction(list_getitem_patched_method, "(OO)", self, elem);
}

static int patched_list_setitem(PyObject *self, PyObject *key, PyObject *value) {
    // NULL in value means list.__delitem__ was called.
    // No need to patch this occurence.
    if (value == NULL){
        return original_list_setitem(self, key, value);
    }

    PyObject* result = PyObject_CallFunction(list_setitem_patched_method, "(OOO)", self, key, value);

    if (!result) {
        // If result is NULL, an error occurred. You should set an appropriate error.
        PyErr_SetString(PyExc_RuntimeError, "Error calling patched __setitem__ method");
        return -1;
    }

    Py_DECREF(result); // Clean up reference to result

    return 0;
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

static PyObject* patch_list_getitem(PyObject* self, PyObject* args) {
    PyObject* patched_method;
    if (!PyArg_ParseTuple(args, "O", &patched_method)) {
        return NULL;
    }
    if (!PyCallable_Check(patched_method)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    Py_XINCREF(patched_method); // Increase reference count

    list_getitem_patched_method = patched_method;

    PyList_Type.tp_as_mapping->mp_subscript = patched_list_getitem;

    Py_RETURN_NONE;
}

static PyObject* patch_list_setitem(PyObject* self, PyObject* args) {
    PyObject* patched_method;
    if (!PyArg_ParseTuple(args, "O", &patched_method)) {
        return NULL;
    }
    if (!PyCallable_Check(patched_method)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    Py_XINCREF(patched_method); // Increase reference count

    if (original_list_setitem == NULL) {
        original_list_setitem = PyList_Type.tp_as_mapping->mp_ass_subscript;
    }

    list_setitem_patched_method = patched_method;

    PyList_Type.tp_as_mapping->mp_ass_subscript = patched_list_setitem;

    Py_RETURN_NONE;
}


static PyMethodDef patchlist_methods[] = {
    {"patch_list_contains", patch_list_contains, METH_VARARGS, "Set the method for list.__contains__ calls."},
    {"patch_list_iter", patch_list_iter, METH_VARARGS, "Set the method for list.__iter__ calls."},
    {"patch_list_getitem", patch_list_getitem, METH_VARARGS, "Set the method for list.__getitem__ calls."},
    {"patch_list_setitem", patch_list_setitem, METH_VARARGS, "Set the method for list.__setitem__ calls."},
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
