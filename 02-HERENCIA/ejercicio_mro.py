class Animal:
    def __init__(self):
        pass
    def comer(self):
        print("Animal comiendo")
    
class Mamifero(Animal):
    def __init__(self):
        pass
    def amamantar(self):
        print("Mamifero amamantando")

class Ave(Animal):
    def __init__(self):
        pass
    def volar(self):
        print("Ave volando")
        
class Murcielago(Mamifero,Ave):
    pass
        
murcielago = Murcielago()
murcielago.comer() # Accede al metodo de la clase Animal 
murcielago.amamantar() #  Accede al método de la clase Mamifero
murcielago.volar() # Ejecutará el método de la clase que lo hereda primero (en este caso Ave) y luego el del padre (Mamifero).
