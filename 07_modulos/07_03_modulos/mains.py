from cuadrado import area_cuadrado, perimetros_cuadrado  #Aqui llamamos el módulo que acabamos de crear

lado = 5 # definimos la var lado    # y contienen las funs q vamos a usar

cuadrado = { #creamos un objeto caudrado de tipo diccionario donde almacenaremos toda las caract del cuadrado
    "lado": lado, #esta guardará el valor del area calculada a partir de la fun
    "area":  area_cuadrado(lado),
    "perimetro": perimetros_cuadrado(lado)

}
print(cuadrado)