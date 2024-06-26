#include <Python.h>
#include <stdio.h>

PyObject* dictionary_getitem_patched_method;
PyObject* dictionary_setitem_patched_method;
PyObject* dictionary_iter_patched_method;

static objobjargproc original_dict_setitem = NULL;


static int patched_dictionary_setitem(PyObject *self, PyObject *key, PyObject *value) {
    // NULL in value means dict.__delitem__ was called.
    // No need to patch this occurence.
    if (value == NULL){
        return original_dict_setitem(self, key, value);
    }

    PyObject* result = PyObject_CallFunction(dictionary_setitem_patched_method, "(OOO)", self, key, value);

    if (!result) {
        // If result is NULL, an error occurred. Set an error.
        PyErr_SetString(PyExc_RuntimeError, "Error calling patched __setitem__ method");
        return -1;
    }

    Py_DECREF(result); // Clean up reference to result

    return 0;
}

static PyObject *patched_dictionary_getitem(PyObject *self, PyObject* key) {
    return PyObject_CallFunction(dictionary_getitem_patched_method, "(OO)", self, key);
}

static PyObject* patched_dictionary_iter(PyObject *self) {
    return PyObject_CallFunction(dictionary_iter_patched_method, "(O)", self);
}

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

    if (original_dict_setitem == NULL) {
        original_dict_setitem = PyDict_Type.tp_as_mapping->mp_ass_subscript;
    }

    dictionary_setitem_patched_method = patched_method;

    PyDict_Type.tp_as_mapping->mp_ass_subscript = patched_dictionary_setitem;

    Py_RETURN_NONE;
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

    dictionary_iter_patched_method = patched_method;

    PyDict_Type.tp_iter = patched_dictionary_iter;

    Py_RETURN_NONE;
}


static PyMethodDef patchdictionary_methods[] = {
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
