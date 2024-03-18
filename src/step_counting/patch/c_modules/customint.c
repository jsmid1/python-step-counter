#include <Python.h>
#include <stdio.h>

PyObject* int_richcompare_patched_method;


static PyObject* patched_int_richcompare(PyObject *self, PyObject *other, int operation) {
    PyObject* result = PyObject_CallFunction(int_richcompare_patched_method, "(OOI)", self, other, operation);

    return result;
}

static PyObject* patch_int_richcompare(PyObject* self, PyObject* args) {
    PyObject* patched_method;
    if (!PyArg_ParseTuple(args, "O", &patched_method)) {
        return NULL;
    }
    if (!PyCallable_Check(patched_method)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    Py_XINCREF(patched_method); // Increase reference count

    int_richcompare_patched_method = patched_method;
    
    PyLong_Type.tp_richcompare = patched_int_richcompare;

    Py_RETURN_NONE;
}

static PyObject* int_add(PyObject* self, PyObject* args) {
    PyObject *a, *b;

    if (!PyArg_ParseTuple(args, "OO", &a, &b)) {
        return NULL;
    }

    if (!PyLong_Check(a) || !PyLong_Check(b)) {
        PyErr_SetString(PyExc_TypeError, "Both arguments must be integers.");
        return NULL;
    }

    return PyLong_Type.tp_as_number->nb_add(a, b);
}

static PyMethodDef patchint_methods[] = {
    {"int_add", int_add, METH_VARARGS, "int_add"},
    {"patch_int_richcompare", patch_int_richcompare, METH_VARARGS, "Set the method for int comparison calls."},
    {NULL, NULL, 0, NULL} // Sentinel, keep this for Python interpreter orientation
};


PyMODINIT_FUNC PyInit_patchint(void) {
    static struct PyModuleDef modDef = {
        PyModuleDef_HEAD_INIT,
        "patchint",
        "Module to patch int comparison methods",
        -1,
        patchint_methods, 
        NULL, NULL, NULL,
        NULL
    };

    PyObject *module = PyModule_Create(&modDef);
    if (!module) {
        return NULL;
    }

    return module;
}
