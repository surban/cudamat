import pdb
import warnings
import ctypes as ct
import numpy as np
from cudamat import generate_exception

_cudalearn = ct.cdll.LoadLibrary('libcudalearn.so')

_cudalearn.mult_by_sigmoid_deriv.restype = ct.c_int


def mult_by_sigmoid_deriv(target, acts):
    err_code = _cudalearn.mult_by_sigmoid_deriv(target.p_mat, acts.p_mat)
    if err_code:
        raise generate_exception(err_code)
