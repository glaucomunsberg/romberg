from __future__ import division, print_function, absolute_import


from scipy.special.orthogonal import p_roots
from scipy.special import gammaln
from numpy import sum, ones, add, diff, isinf, isscalar, \
     asarray, real, trapz, arange, empty
from PrettyTable import *
import numpy as np
import math
import warnings


def vectorize1(func, args=(), vec_func=False):

    if vec_func:
        def vfunc(x):
            return func(x, *args)
    else:
        def vfunc(x):
            if isscalar(x):
                return func(x, *args)
            x = asarray(x)
            # call with first point to get output type
            y0 = func(x[0], *args)
            n = len(x)
            if hasattr(y0, 'dtype'):
                output = empty((n,), dtype=y0.dtype)
            else:
                output = empty((n,), dtype=type(y0))
            output[0] = y0
            for i in xrange(1, n):
                output[i] = func(x[i], *args)
            return output
    return vfunc

def _diferenciaDoTrapezio(function, interval, numtraps):
    """
    Perform part of the trapezoidal rule to integrate a function.
    Assume that we had called difftrap with all lower powers-of-2
    starting with 1.  Calling difftrap only returns the summation
    of the new ordinates.  It does _not_ multiply by the width
    of the trapezoids.  This must be performed by the caller.
        'function' is the function to evaluate (must accept vector arguments).
        'interval' is a sequence with lower and upper limits
                   of integration.
        'numtraps' is the number of trapezoids to use (must be a
                   power-of-2).
    """
    if numtraps <= 0:
        raise ValueError("numtraps must be > 0 in difftrap().")
    elif numtraps == 1:
        return 0.5*(function(interval[0])+function(interval[1]))
    else:
        numtosum = numtraps/2
        h = float(interval[1]-interval[0])/numtosum
        lox = interval[0] + 0.5 * h
        points = lox + h * arange(0, numtosum)
        s = sum(function(points),0)
        return s


def _romberg_diff(b, c, k):
    tmp = 4.0**k
    return (tmp * c - b)/(tmp - 1.0)


def  _printresult(function, interval, resmat):
    # Print the Romberg result matrix.
    matrix = [[0 for x in range(1,9)] for x in xrange(1,9)] 
    table = PrettyTable()
    i = j = 0
    table.field_names = ['Steps','1','2','3','4','5','6','7']
    #print('%6s %9s %9s' % ('Steps', 'StepSize', 'Results'))
    for i in range(len(resmat)):
        #print('%6d %9f' % (2**i, (interval[1]-interval[0])/(2.**i)), end=' ')
       
       # table.add_row([2**i,((interval[1]-interval[0])/(2.**i)),,resmat[i][1],resmat[i][2],resmat[i][3],resmat[i][4],resmat[i][5],resmat[i][6]])
           
        for j in range(i+1):
             matrix[i][j] = resmat[i][j]
            # print('%9f' % (resmat[i][j]), end=' ')
        table.add_row([2**i,matrix[i][0],matrix[i][1],matrix[i][2],matrix[i][3],matrix[i][4],matrix[i][5],matrix[i][6]])
    print(table)
    print('')
    print('Result:', resmat[i][j], end=' ')


def rombergIterate(function, a, b, args=(), tol=1.48e-8, rtol=1.48e-8, show=False, divmax=8, vec_func=False):

    if isinf(a) or isinf(b):
        print(bcolors.FAIL +'Atencion! Limit out of finites' + bcolors.ENDC)

    vfunc = vectorize1(function, args, vec_func=vec_func)
    n = 1
    interval = [a,b]
    intrange = b-a
    ordsum = _diferenciaDoTrapezio(vfunc, interval, n)
    result = intrange * ordsum
    resmat = [[result]]
    err = np.inf

    for i in xrange(1, divmax+1):
        n = n * 2
        ordsum = ordsum + _diferenciaDoTrapezio(vfunc, interval, n)
        resmat.append([])
        resmat[i].append(intrange * ordsum / n)
        for k in range(i):
            resmat[i].append(_romberg_diff(resmat[i-1][k], resmat[i][k], k+1))
        result = resmat[i][i]
        lastresult = resmat[i-1][i-1]

        err = abs(result - lastresult)
        if err < tol or err < rtol*abs(result):
            break
    else:
        warnings.warn(
            "divmax (%d) exceeded. Latest difference = %e" % (divmax, err),
            AccuracyWarning)

    if show:
         _printresult(vfunc, interval, resmat)
    return result
