
from .a cimport a_fun

cpdef b_fun(int a, int b):
    return a_fun(a, b)
