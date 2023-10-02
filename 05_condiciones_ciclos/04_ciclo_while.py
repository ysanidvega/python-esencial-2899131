# Ciclo while . Para iterar en pyton tenemos el ciclo for y el ciclo while en el caso de una lista
i = 1
while 1 <= 5:
    print(i)
    i += 1


# Uso de la instrucción break
i = 1
while 1 <= 5:
    if i == 3: # el contador es igaul a 3, por lo que en 3 va a para la iteración
        break
    print(i)
    i += 1


# Uso de la instrucción continue
i = 1
while 1 <= 5:
    if i == 3:
        continue
    print(i)
    i += 1
