class Persona: #Cada objeto que creamos a partir de una clase en python puede tener atributos
    atributo = 123 #Existen atributo de instancia y atributo de la clase. El 1º se definen dentro de la 
                   #fun init, en este caso serán nombre y edad como atributos de instancias

    def __init__(self, nombre, edad):
        self.nombre = nombre # self.nombre para declarar q ese nombre va a ser de toda la clase y le asignamos 
        self.edad = edad #parametro nombre q recibimos del constructor


paco = Persona(nombre="Paco", edad=20)
print(paco.nombre)
print(paco.edad)
print(paco.atributo)
