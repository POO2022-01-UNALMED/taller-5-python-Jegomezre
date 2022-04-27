from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0
    
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, pelaje = None, patas = None):
        super().__init__(nombre=nombre, edad=edad, habitat=habitat, genero=genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)
    @classmethod
    def crearCaballo(self, nombre, edad, genero):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)
    @classmethod
    def crearLeon(self, nombre, edad, genero):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)

    def cantidadMamiferos(self):
        return len(self.listado)
           
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    def isPelaje(self):
        return self._pelaje  
    
    def setPatas(self, patas):
        self._patas = patas
    def getPatas(self):
        return self._patas 