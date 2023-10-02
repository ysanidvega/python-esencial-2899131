# Iterar un string. Los ciclos for nos permiten iterar sobre diferentes estructura de datos e incluso sobre strg
for letra in "Texto":
    print(letra)


# Iterar una lista
lenguajes = ["python", "java", "javascript", "golang"]
for elemento in lenguajes:
    print(elemento)


# La instrucción break rompe el ciclo
lenguajes = ["python", "java", "javascript", "golang"]
for elemento in lenguajes:
    print(elemento)
    break


# Instrucción break dentro de una condición
lenguajes = ["python", "java", "javascript", "golang"]
for elemento in lenguajes:
    if elemento == "javascript":
        break
print(elemento)


# Instrucción continue dentro de una condición
lenguajes = ["python", "java", "javascript", "golang"]
for elemento in lenguajes:
    if elemento == "javascript":
        continue
print(elemento)


# Función range()
for element in range(1, 6):
    print(element)

    i = 0 # la primera posicion del elemento 
    while i < len(lenguajes):
        print(lenguajes[i]) #imprima lenguaje en la posicion del contador
        i += 1                     # posteriormente incremente el contador en 1. Va subiendo desde 0 
