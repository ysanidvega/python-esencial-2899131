class Persona: #el palno q nos permite construir a la persona es un plano q se llama clase
    pass  #el nombre la clase es persona. Impide q paython me genero error al escibir P en mayuscula


pedro = Persona()# creamos el objeto persona llamado Pedro y lo invocamos con el parentesis
print(type(pedro))# imprimimos el tipo de Pedro, guardamos y ejecutamos el programa

paco = Persona()# hacemos lo mismo con Paco para confirmar q pertenece a la misma clase persona
print(type(paco))

print(pedro == paco)# Son objeto diferente aunque sean del mismo tipo de objeto
