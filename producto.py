class Producto:
    
    '''--------------------------------------------
    # Atributos
    -------------------------------------------------'''
    
    nombreProducto = ""
    precioProducto = 0
    cantidadProducto = 0
    cantidadAbastecimiento = 0
    cantidadMinima = 0
    
    
    '''-------------------------------------------------------
    # 1 = Papelería, 2 = Supermercado, 3 = Drogueria
    ----------------------------------------------------------'''

    tipoProducto = 0
    
    '''-----------------------------------------------------
    # metodos
    --------------------------------------------------------'''
    
    def __init__(self):
        self.cantidadAbastecimiento = 0
        self.cantidadProducto = 0
        self.nombreProducto = ""
        self.precioProducto = 0
        self.tipoProducto = 0
        self.cantidadMinima = 0
        
    def Abastecer(self,cantidad):
        if self.cantidadAbastecimiento <= self.cantidadMinima:
            self.cantidadProducto = self.cantidadProducto + cantidad
            
            
    def CambiarProducto(self, NombreActual, nNombre, nTipo, nPrecio, nCantidadAbastecimiento, nCantidadMinima):
        self.nombreProducto[NombreActual] = nNombre
        self.precioProducto = nPrecio
        self.tipoProducto = nTipo
        self.cantidadAbastecimiento = nCantidadAbastecimiento
        self.cantidadMinima = nCantidadMinima
        
