def bisection(func, a, b, eps=1e-8):
    while True:
        x = (a + b) / 2
        fx = func(x)
        if -eps < fx < eps:
            return x
        fa = func(a)
        if fx * fa < 0:
            b = x
        else:
            a = x

def newton_raphson(func_f, func_g, x=0, eps=1e-8):
    while True:
        fx, gx = func_f(x), func_g(x)
        if -eps < fx < eps:
            return x
        x -= fx / gx
