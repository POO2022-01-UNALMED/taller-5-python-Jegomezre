from zooAnimales.animal import Animal

class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, color= None, venenoso = None):
        super().__init__(nombre=nombre, edad=edad, habitat=habitat, genero=genero)
        self._colorPiel = color
        self._venenoso = venenoso
        Anfibio.listado.append(self)

    @classmethod
    def crearRana(self, nombre, edad, genero):
        self.ranas += 1
        return Anfibio(nombre, edad, "selva", genero,"rojo",True)
    @classmethod
    def crearSalamandra(self, nombre, edad, genero):
        self.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero,"negro y amarillo",False)   
    
    def setColorPiel(self, color):
        self._colorPiel = color
    def getColorPiel(self):
        return self._colorPiel
    def setVenenoso(self, ven):
        self._venenoso = ven
    def isVenenoso(self):
        return self._venenoso