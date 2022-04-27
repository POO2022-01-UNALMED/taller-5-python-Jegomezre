from zooAnimales.animal import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0
    
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, color= None, cantidad = None):
        super().__init__(nombre=nombre, edad=edad, habitat=habitat, genero=genero)
        self._colorEscamas = color
        self._cantidadAletas = cantidad
        Pez.listado.append(self)
    @classmethod
    def crearSalmon(self, nombre, edad, genero):
        self.salmones += 1
        return Pez(nombre, edad, "oceano", genero,"rojo",6)
    @classmethod
    def crearBacalao(self, nombre, edad, genero):
        self.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero,"gris",6)
    
    
    def setColorEscamas(self, color):
        self._colorEscamas = color
    def getColorEscamas(self):
        return self._colorEscamas

    def setCantidadAletas(self, color):
        self._cantidadAletas = color
    def getCantidadAletas(self):
        return self._cantidadAletas