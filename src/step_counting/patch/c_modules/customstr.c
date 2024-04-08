#include <Python.h>
#include <stdio.h>

PyObject* str_getitem_patched_method;


static PyObject *patched_str_getitem(PyObject *self, PyObject * elem) {
    return PyObject_CallFunction(str_getitem_patched_method, "(OO)", self, elem);
}


static PyObject* patch_str_getitem(PyObject* self, PyObject* args) {
    PyObject* patched_method;
    if (!PyArg_ParseTuple(args, "O", &patched_method)) {
        return NULL;
    }
    if (!PyCallable_Check(patched_method)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    Py_XINCREF(patched_method); // Increase reference count

    str_getitem_patched_method = patched_method;

    PyUnicode_Type.tp_as_mapping->mp_subscript = patched_str_getitem;

    Py_RETURN_NONE;
}

static PyMethodDef patchstr_methods[] = {
    {"patch_str_getitem", patch_str_getitem, METH_VARARGS, "Set the method for tuple.__getitem__ calls."},
    {NULL, NULL, 0, NULL} // Sentinel, keep this for Python interpreter orientation
};


PyMODINIT_FUNC PyInit_patchstr(void) {
    static struct PyModuleDef modDef = {
        PyModuleDef_HEAD_INIT,
        "patchstr",
        "Module to patch tuple methods",
        -1,
        patchstr_methods, 
        NULL, NULL, NULL,
        NULL
    };

    PyObject *module = PyModule_Create(&modDef);
    if (!module) {
        return NULL;
    }

    return module;
}
