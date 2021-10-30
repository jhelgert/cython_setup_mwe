
from my_package import foo
from my_package.b import b_fun


def test_b_fun():
    """ tests a cpdef cython function """
    assert b_fun(1, 2) == 3


def test_foo():
    """ tests a regular python function """
    assert foo() == 3
