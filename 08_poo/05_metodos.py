class Persona: #Los métodos son funciones que se definen dentro de una clase

    def __init__(self, nombre, edad):#Los metodos de clases se definen tal como las funciones pero los metodos
        self.nombre = nombre # deben recibir como 1º atributo la var self, la cual representa la instancia
        self.edad = edad #de la clase y a traves de ella se puede acceder a las propiedades y funciones de
    def cumplir_anios(self): # la clase
        self.edad += 1
        print(f"Feliz Cumpleaños #{self.edad}")


paco = Persona(nombre="Paco", edad=20)
paco.cumplir_anios()
