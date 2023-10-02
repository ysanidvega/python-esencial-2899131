lenguaje = {     #Creamos el diccionario llamado lenguaje
    "nombre": "python",
    "creador": "Guido Van Rossum" 
}


# Iterar un diccionario. Podemos iterar sobre un diccionario usando el ciclo for. Contienen una llave y valor)
for llave in lenguaje: # Creamos nuestro ciclo for para la llave en en lnguaje, imprimimos la llave con su valor
    print(llave)
    print(lenguaje[llave])


for llave in lenguaje:
    print("llave:", llave)
    print("valor", lenguaje[llave])

# Iterar un diccionario usando keys(). Launción keys retorna una lista con las llaves del dicc
for valor in lenguaje.keys(): #para el elem en lenguaje .keys, imprimimos el elem, e imprimirá
    print(valor) # las llaves que teniamos en el dicc


# Iterar un diccionario usando values(). Aqui imprimimos sus valores
for valor in lenguaje.values():
    print(valor)


# Iterar un diccionario usando items(). esta funcion retorna dos valores. Debemos capturar 2 valores en el 
for llave, valor in lenguaje.items(): #iterador
    print(llave, valor)
