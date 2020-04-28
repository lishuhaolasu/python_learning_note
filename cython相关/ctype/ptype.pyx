import time


def f(x):
    return x**2 - x


def intergrate_f(a, b, N):
    start_time = time.time()
    s = 0
    dx = (b-a) / N
    for i in range(N):
        s += f(a+i*dx)
    ret = s*dx
    print(time.time()-start_time)
    return ret

intergrate_f(100000,100000,1100000)