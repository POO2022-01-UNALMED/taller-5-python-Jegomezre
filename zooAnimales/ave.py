from zooAnimales.animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0 
    aguilas = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPlumas = None):
        super().__init__(nombre=nombre, edad=edad, habitat=habitat, genero=genero)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")
    
    @classmethod
    def crearAguila(self, nombre, edad, genero):
        self.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    def getColorPlumas(self):
        return self._colorPlumas  