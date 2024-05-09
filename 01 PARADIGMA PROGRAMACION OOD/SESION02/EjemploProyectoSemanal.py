import math

def calculoPi():

    divisiones = 10000

    cuarto_area = 0.0
    acumulador = 0

    for i in range(divisiones):
        acumulador += 1
        base_triangulo = float(acumulador)/float(divisiones)
        altura = math.sqrt(1-base_triangulo*base_triangulo)
        base = 1 / float(divisiones)
        #print(base, "-",altura)
        cuarto_area += base*altura 

    return cuarto_area * 4

print("Dame el diametro del circulo")
diametro = float(input())
radio = diametro / 2
area = calculoPi() * radio * radio
print("el area es:", area)
print(area)
