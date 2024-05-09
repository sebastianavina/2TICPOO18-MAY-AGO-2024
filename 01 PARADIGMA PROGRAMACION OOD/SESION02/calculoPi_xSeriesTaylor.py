acumulador = 0.0

contador = 0
division_actual = 1.0
essuma = True

while division_actual > 0.00052:
    contador += 1
    division_actual = 1/contador
    
    if contador % 2 != 0:
        if essuma:
            acumulador += division_actual
        else:
            acumulador -= division_actual
        essuma = not essuma

    
print("el cuarto del area es: ", acumulador)

pi=acumulador * 4

print("pi es igual a", pi)
