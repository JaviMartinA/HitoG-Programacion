from abc import *

class Animal(ABC):
    def comiendo(self):
        print("El animal esta comiendo.")

class Perro(Animal):
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
    def comiendo(self):
        print(f"El perro {self.nombre}, de raza {self.raza} y de edad {self.edad} años esta comiendo.")

#Se instancia pero no se puede usar porque es una clase abstracta
animal = Animal()
animal.comiendo

perro = Perro("Pepe", "Bichón maltés", 10)
perro.comiendo()