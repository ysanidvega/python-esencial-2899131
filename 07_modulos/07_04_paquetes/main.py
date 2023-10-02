from figuras.cuadrado import area_cuadrado, perimetro_cuadrado #Llamamos la carpeta figura y las funciones que contiene
from figuras.circulo import area_circulo, perimetro_circulo


lado = 5
cuadrado = { #creamos el objeto llamado cuadrado
    "lado": lado,
    "area": area_cuadrado(lado),
    "perimetro": perimetro_cuadrado(lado)
}
print(cuadrado)

radio= 5
circulo = {
    "radio": radio,
    "area": area_circulo(radio),
    "perimetro": perimetro_circulo(radio)
}
print(circulo)

radio = 10
circulo_2 = {
    "radio": radio,
    "area":area_circulo(radio),
    "perimetro": perimetro_circulo(radio)
}
print(circulo_2)
