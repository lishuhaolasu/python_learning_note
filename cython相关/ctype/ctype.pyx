import time


def f(double x):
    return x ** 2 - x


def intergrate_f(double a, double b, int N):
    cdef int i
    cdef double s, dx, ret, start_time
    start_time = time.time()
    s = 0
    dx = (b-a) / N
    for i in range(N):
        s += f(a+i*dx)
    ret = s*dx
    print(time.time()-start_time)
    return ret
