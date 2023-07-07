import math

def bisection_method(f, a, b, tolerance, max_iterations):
    if f(a) * f(b) >= 0:
        print(f" a={a}, b={b}")
        print(f" c = ({a} + {b}) / 2")
        c = (a + b) / 2
        print(f" c = {c}")
        print("El método de la bisección no es aplicable en el intervalo dado.")
        print(" f(c) * f(a) ")
        print(" f(c) ", f(c))
        print(" f(a) ", f(a))
        print(  f(c) * f(a))
        return None

    iteration = 1
    while iteration <= max_iterations:
        # Aproximar la raiz paso 2
        c = (a + b) / 2
        print(f"Iteración {iteration}: ")
        print(f" a={a}, b={b}")
        print(f" c = ({a} + {b}) / 2")
        print(f" c = {c}")

        if abs(f(c)) < tolerance:
            return c
        # Si mayor o menor a cero , decidiendo los 
        # nuevos limites o intervalos
        print(" f(c) * f(a) ")
        print(" f(c) ", f(c))
        print(" f(a) ", f(a))
        print(  f(c) * f(a))
        if f(c) * f(a) < 0:
            b = c
            print("  change to b for", c)
        else:
            a = c
            print("  change to a for",  c)


        iteration += 1

    print("No se pudo encontrar una solución dentro del número máximo de iteraciones.")
    return None

# Definición de las ecuaciones no lineales
equations = [
    lambda x: math.log(x - 2),
    lambda x: math.exp(-x),
    lambda x: math.exp(x) - x,
    lambda x: 10 * math.exp(x/2) * math.cos(2*x) - 4,
    lambda x: x**2 - 2,
    lambda x: x**3 - 2,
    lambda x: x * math.cos(x) + math.sin(x * 2) - 2,
    lambda x: x**3 + 4*x**2 - 10
]
intervals = [
    (2.1, 5),
    (0, 1), # No tiene raiz real
    (-0.5, 1), # No tiene raiz real
    (0, 1),
    (1.2, 2),
    (1, 1.5),
    (4, 6),
    (1, 2)
]
# Parámetros del método de la bisección
tolerance = 0.001
max_iterations = 100


# Resolución de las ecuaciones utilizando el método de la bisección
for i in range(len(equations)):
    equation = equations[i]
    interval = intervals[i]
    print(f"------------------Resolviendo ecuación #{i+1}:")
    root = bisection_method(equation, interval[0], interval[1], tolerance, max_iterations)
    if root is not None:
        print(f"La raíz encontrada es: {root}\n")
