from producto import Producto

class Tienda:
    
    '''------------------------------------------------------
    # Metodos
    ---------------------------------------------------------'''
    
    def __init__(self):
        self.__producto1 = Producto("PAPELERIA", "lapiz", 500, 30, 9)
        self.__producto2 = Producto ("PAPELERIA", "borrador", 300, 15, 5)
        self.__producto3 = Producto ("SUPERMERCADO", "cafe", 5600, 20, 10)
        self.__producto4 = Producto ("FARMACIA", "desinfectante", 3200, 12, 11)
        self.__dineroEnCaja = 0
    
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

    def venderProducto(self,pNombreProducto, pCantidad):
        if pNombreProducto == self.__producto1.__nombre:
            self.__producto1.vender(pCantidad)
        elif pNombreProducto == self.__producto2.__nombre:
            self.__producto2.vender(pCantidad)
        elif pNombreProducto == self.__producto3.__nombre:
            self.__producto3.vender(pCantidad)
        elif pNombreProducto == self.__producto4.__nombre:
            self.__producto4.vender(pCantidad)
            
    def cuantosPapelerias(self):
        return self.__producto1.getCantidadUnidadesVendidas() +  self.__producto2.getCantidadUnidadesVendidas()
        
    


