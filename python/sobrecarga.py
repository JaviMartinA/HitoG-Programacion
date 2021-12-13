class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def comer(self, nombre = None, hora = None):
        if hora is None and nombre is None: 
            print("Persona comiendo")
            
        elif hora is not None and nombre is not None:
            print(f"{nombre} comiendo a las {hora} h")
            


Persona = Persona("Federico", 18)
#Sobrecarga
Persona.comer("Federico", "18:00")
Persona.comer()