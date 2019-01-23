
LOAD_CONST #push 对象进 value stack
"""
case LOAD_CONST:
    x = GETITEM(consts, oparg);
    Py_INCREF(x);
    PUSH(x);
    goto fast_next_opcode;
"""

LOAD_NAME
"""
case LOAD_NAME:
    w = GETITEM(names, oparg);
    if ((v = f->f_locals) == NULL) {
        PyErr_Format(PyExc_SystemError,
                     "no locals when loading %s",
                     PyObject_REPR(w));
        why = WHY_EXCEPTION;
        break;
    }
    if (PyDict_CheckExact(v)) {
        x = PyDict_GetItem(v, w);
        Py_XINCREF(x);
    }
    else {
        x = PyObject_GetItem(v, w);
        if (x == NULL && PyErr_Occurred()) {
            if (!PyErr_ExceptionMatches(
                            PyExc_KeyError))
                break;
            PyErr_Clear();
        }
    }
    if (x == NULL) {
        x = PyDict_GetItem(f->f_globals, w);
        if (x == NULL) {
            x = PyDict_GetItem(f->f_builtins, w);
            if (x == NULL) {
                format_exc_check_arg(
                            PyExc_NameError,
                            NAME_ERROR_MSG, w);
                break;
            }
        }
        Py_INCREF(x);
    }
    PUSH(x);
            continue;
"""
SETUP_LOOP #
