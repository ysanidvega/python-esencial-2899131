from cuadrado import area_cuadrado, perimetro_cuadrado


lado = 5
cuadrado = { # Creamos el objeto cuadrado de tipo dicc, donde almacenamos las caract del cuadrado
"lado": lado, # la 1º llave se llama lado y le asignamos el valor de la var lado 
"area": area_cuadrado(lado), # llamamos la func y le pasamos el param lado 
                                  # el resultado se va a guardar en la llave área
"perimetro": perimetro_cuadrado(lado) # llamamos la func del perimetro y le enviamos la variable lado
                                         # para que calcule el resultado
}

print(cuadrado) # Imprimimos el objeto cuadrado que es un diccionario
perimetro = perimetro_cuadrado(lado) # En vez de guardar los datos en un dicc, lo podemos asignar a una var
print(perimetro) 










