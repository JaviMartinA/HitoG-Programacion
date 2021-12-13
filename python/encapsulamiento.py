class Empleado():
    def __init__(self, nombre):
        self.__nombre = nombre
    def Nombre(self):
        print(f"Se llama {self.__nombre}")

empleado = Empleado("Juan")

#print(empleado.__nombre)
#No funciona si se ejecuta porque necesita un metodo para sacar el atributo

empleado.Nombre()