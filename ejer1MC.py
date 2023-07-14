import random
import math
import matplotlib.pyplot as plt

def monte_carlo_area_elipse(a, b, m):
    sa = 0  # Suma de las áreas calculadas en cada iteración
    saa = 0  # Suma de los cuadrados de las áreas calculadas en cada iteración

    px = []  # Lista para almacenar los valores de x dentro de la elipse
    py = []  # Lista para almacenar los valores de y dentro de la elipse

    for _ in range(m):
        n = 0  # Contador de puntos dentro de la elipse

        for _ in range(m):
            x = random.uniform(-a, a)  # Generar un número aleatorio en el rango [-a, a]
            y = random.uniform(-b, b)  # Generar un número aleatorio en el rango [-b, b]

            if (x**2 / a**2) + (y**2 / b**2) < 1:  # Verificar si el punto (x, y) está dentro de la elipse
                n += 1  # Incrementar el contador de puntos dentro de la elipse
                px.append(x)  # Almacenar el valor de x
                py.append(y)  # Almacenar el valor de y

        area = n * (2*a) * (2*b) / m  # Calcular el área estimada para la iteración actual
        sa += area  # Sumar el área a la suma acumulada de áreas
        saa += area**2  # Sumar el cuadrado del área a la suma acumulada de los cuadrados de áreas

    prom = sa / m  # Calcular el promedio de áreas estimadas
    desv = math.sqrt(m * saa - sa**2) / m  # Calcular la desviación estándar de las áreas estimadas

    # Graficar los puntos dentro de la elipse
    plt.plot(px, py, '.', markersize=1)
    plt.title('Puntos dentro de la elipse por el método Monte Carlo')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis([-a, a, -b, b])  # Establecer los límites de los ejes
    plt.show()

    return prom, desv

# Ejemplo de uso
a = 2  # Semieje mayor de la elipse
b = 3  # Semieje menor de la elipse
m = 10000  # Número de iteraciones

promedio, desviacion = monte_carlo_area_elipse(a, b, m)
print("Área estimada:", promedio)
print("Desviación estándar:", desviacion)
