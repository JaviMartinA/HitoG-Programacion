from typing import overload


class Persona(object):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrarNombre(self):
        print(f"Persona es {self.nombre}.")
    def mostrarNombre(self):
        print(f"El nombre de la Persona es {self.nombre}.")
class Clase():
    clase = "DAM"

class Alumno(Persona, Clase):
    #overwrite
    def mostrarNombre(self):
        print(f"El nombre del estudiante es {self.nombre} de la clase de {self.clase}.")

#Clase Padre
Persona = Persona("Juan", 18)
Persona.mostrarNombre()

#Clase Hija con Herencia múltiple
Alumno = Alumno("Juan", 18)
Alumno.mostrarNombre()
