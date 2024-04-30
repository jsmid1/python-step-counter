#include <Python.h>
#include <stdio.h>

PyObject* bytearray_setitem_patched_method;

static objobjargproc original_bytearray_setitem = NULL;

static int patched_bytearray_setitem(PyObject *self, PyObject *key, PyObject *value) {
    // NULL in value means bytearray.__delitem__ was called.
    // No need to patch this occurence.
    if (value == NULL){
        return original_bytearray_setitem(self, key, value);
    }

    PyObject* result = PyObject_CallFunction(bytearray_setitem_patched_method, "(OOO)", self, key, value);

    if (!result) {
        // If result is NULL, an error occurred. You should set an appropriate error.
        PyErr_SetString(PyExc_RuntimeError, "Error calling patched __setitem__ method");
        return -1;
    }

    Py_DECREF(result); // Clean up reference to result

    return 0;
}

static PyObject* patch_bytearray_setitem(PyObject* self, PyObject* args) {
    PyObject* patched_method;
    if (!PyArg_ParseTuple(args, "O", &patched_method)) {
        return NULL;
    }
    if (!PyCallable_Check(patched_method)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    Py_XINCREF(patched_method); // Increase reference count

    if (original_bytearray_setitem == NULL) {
        original_bytearray_setitem = PyByteArray_Type.tp_as_mapping->mp_ass_subscript;
    }

    bytearray_setitem_patched_method = patched_method;

    PyByteArray_Type.tp_as_mapping->mp_ass_subscript = patched_bytearray_setitem;

    Py_RETURN_NONE;
}


static PyMethodDef patchbytearray_methods[] = {
    {"patch_bytearray_setitem", patch_bytearray_setitem, METH_VARARGS, "Set the method for bytearray.__setitem__ calls."},
    {NULL, NULL, 0, NULL} // Sentinel, keep this for Python interpreter orientation
};


PyMODINIT_FUNC PyInit_patchbytearray(void) {
    static struct PyModuleDef modDef = {
        PyModuleDef_HEAD_INIT,
        "patchbytearray",
        "Module to patch bytearray methods",
        -1,
        patchbytearray_methods, 
        NULL, NULL, NULL,
        NULL
    };

    PyObject *module = PyModule_Create(&modDef);
    if (!module) {
        return NULL;
    }

    return module;
}
