from typing import overload


class Division(object):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2 
    def resultado(self):
        return int(self.n1 / self.n2)
    
#Devuele un int
division = Division(8,2)
print(f"El resultado es {division.resultado()}")
#También devuele un int, aunque el retorno sea un float ya que cambia el formato
division = Division(7,2)
print(f"El resultado es {division.resultado()}")
