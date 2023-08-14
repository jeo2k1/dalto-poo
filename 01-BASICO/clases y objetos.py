class Celular(): # clase Celular
    def __init__(self, marca, modelo, camara): #constructor __init__ y atributos
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self): # metodo llamar
        print(f'Estas realizando una llamada desde: {self.modelo}')
        
    def cortar(self): # metodo cortar
        print(f'Cortarste la llamada desde: {self.modelo}')        
    
celular1 = Celular("Samsung","S23","48MP") # creando una instancia celular1 de la clase Celular
celular2 = Celular("Apple","Iphone 15 Pro","56MP") # creando una instancia celular2 de la clase Celular

celular1.llamar() # llamo al metodo llamar