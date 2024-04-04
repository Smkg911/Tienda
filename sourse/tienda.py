from producto import Producto

class Tienda:
    
    
    '''--------------------------------------------
    # Atributos
    -------------------------------------------------'''
    
    __producto1 = None 
    __producto2 = None
    __producto3 = None
    __producto4 = None
    __dineroEnCaja = 0.0
    
    '''------------------------------------------------------
    # Metodos
    ---------------------------------------------------------'''
    
    def __init__(self):
        self.__producto1 = Producto
        self.__producto2 = Producto  
        self.__producto3 = Producto  
        self.__producto4 = Producto  
    
    def getProducto1(self):
        return self.__producto1
    
    def getProducto2(self):
        return self.__producto2
    
    def getProducto3(self):
        return self.__producto3
    
    def getProducto4(self):
        return self.__producto4

    def getDineroEnCaja(self): 
        return self.__dineroEnCaja
    


