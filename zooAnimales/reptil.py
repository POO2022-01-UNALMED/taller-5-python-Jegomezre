from zooAnimales.animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, color= None,largo = None):
        super().__init__(nombre=nombre, edad=edad, habitat=habitat, genero=genero)
        self._colorEscamas = color
        self._largoCola = largo
        Reptil.listado.append(self)

    @classmethod
    def crearIguana(self, nombre, edad, genero):
        self.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @classmethod
    def crearSerpiente(self, nombre, edad, genero):
        self.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        
    def setColorEscamas(self, color):
        self._colorEscamas = color
    def getColorEscamas(self):
        return self._colorEscamas

    def setLargoCola(self, largo):
        self._largoCola = largo
    def getLargoCola(self):
        return self._largoCola  