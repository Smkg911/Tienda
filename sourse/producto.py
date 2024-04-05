from enum import Enum 

'''----------------------------------------------------------------
# Enumeraciones
--------------------------------------------------------------------'''
class Tipo(Enum):
    
    '''--------------------------------------------------------------
    # Enumeraciones
    ------------------------------------------------------------------'''
    
    PAPELERIA = 1
    SUPERMERCADO = 2
    FARMACIA = 3

class Producto: 
    
    '''--------------------------------------------
    # Constantes
    -------------------------------------------------'''
    
    __IVA_PAPELERIA = 0.16
    __IVA_SUPERMERCADO = 0.04
    __IVA_FARMACIA = 0.12

    '''-----------------------------------------------------
    # metodos
    --------------------------------------------------------'''
    
    def __init__(self, pTipo, pNombre, pValorUnitario, pCantidadBodega, pCantidadMinima):
        self.__tipo = pTipo
        self.__nombre = pNombre
        self.__valorUnitario = pValorUnitario
        self.__cantidadBodega = pCantidadBodega
        self.__cantidadMinima = pCantidadMinima
        self.__cantidadUnidadesVendida = 0
        
    def getNombre(self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo
    
    def getValorUnitario(self):
        return self.__valorUnitario
    
    def getCantidadBodega(self):
        return self.__cantidadBodega
    
    def getCantidadMinima(self):
        return self.__cantidadMinima
    
    def getCantidadUnidadesVendidas(self):
        return self.__cantidadUnidadesVendida
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setTipo(self,tipo):
        self.__tipo = tipo 
        
    def setValorUnitario(self,valorUnitario):
        self.__valorUnitario = valorUnitario 
        
    def setCantidadBodega(self,cantidadBodega):
        self.__cantidadBodega = cantidadBodega
        
    def setCantidadMinima(self,cantidadMinima):
        self.__cantidadMinima = cantidadMinima
        
    def setCantidadUnidadesVendidas(self,cantidadUnidadesVendidas):
        self.__cantidadUnidadesVendida = cantidadUnidadesVendidas
         
    def vender(self,cantidad):
        if cantidad <= self.__cantidadBodega:
            self.__cantidadUnidadesVendida += cantidad
            self.__cantidadBodega -= cantidad
        else: 
            print ("Cantidad no disponible")
        
    def haySuficiente(self, cantidad):
        if cantidad <= self.__cantidadBodega:
            return True
        else:
            return False
        # return cantidad <= self.__cantidadBodega 
        
    def getIVA(self):
        if self.__tipo == "PAPELERIA":
            return self.__IVA_PAPELERIA
        elif self.__tipo == "FARMACIA":
            return self.__IVA_FARMACIA
        elif self.__tipo == "SUPERMERCADO":
            return self.__IVA_SUPERMERCADO
        else:
            print ("Categoria no soportada")
    
    def aumento(self):
        if self.__valorUnitario < 1000:
            self.__valorUnitario *= 1.01
        elif self.__valorUnitario <= 1000 and self.__valorUnitario <= 5000:
            self.__valorUnitario *= 1.02
        elif self.__valorUnitario > 5000:
            self.__valorUnitario *= 1.03
    
    def hacerPedido(self, cantidad):
        if self.__cantidadBodega <= self.__cantidadMinima:
            self.__cantidadBodega += cantidad
            
    def cambiarValorUnitario(self):
        if self.__tipo == "PAPELERIA" or self.__tipo == "FARMACIA":
            self.__valorUnitario -= (self.__valorUnitario * 0.1)
        elif self.__tipo == "SUPERMERCADO":
            self.__valorUnitario += (self.__valorUnitario * 0.05)
    
