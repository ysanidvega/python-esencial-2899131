class Persona: # La herencia de clase permite q una clase sea creada a partir de otra.
               #La clase padre o clase principal es la clase persona q tiene como atributo nombre
            
    def __init__(self, nombre, edad):# y edad y el método cumplir años
        self.nombre = nombre
        self.edad = edad

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz Cumpleaños #{self.edad}")


class Empleado(Persona): # En la clase hijo ponemos Persona que es clase padre del cual heredará los atributos

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)#Super nos permite heredar los atributos de la clase persona

    def trabajar(self, horas_trabajadas):
        print(f"{self.nombre} ha trabajado {horas_trabajadas} horas")


paco = Empleado(nombre="Paco", edad=20)
paco.trabajar(horas_trabajadas= 16)

