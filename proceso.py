tolerance = 0.001
max_iterations = 100
equation = lambda x: -0.5*x**2 + 2.5*x+4.5
a = 6
b = 7
def bisection_method(f, a, b, tolerance):
    iteration = 1
    while iteration <= max_iterations:
        print("------------- iteracion ",iteration)
        print("a nuevo: ", a)
        print("b nuevo: ", b)
        # Aproximar la raiz paso 2
        c = (a + b) / 2
        if abs(f(c)) < tolerance:
            return c
        # Si mayor o menor a cero , decidiendo los 
        # nuevos limites o intervalos
        print("f(c) * f(a): ",f(c) * f(a))

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteration += 1

        print("a nuevo: ", a)
        print("b nuevo: ", b)
        print("c raiz apox: ", c)

bisection_method(equation, a, b, tolerance)
