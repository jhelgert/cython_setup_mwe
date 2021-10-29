
from .a cimport a_fun

cdef b_fun(int a, int b):
    return a_fun(a, b)

def b_py_fun(a, b):
    return b_fun(a, b)