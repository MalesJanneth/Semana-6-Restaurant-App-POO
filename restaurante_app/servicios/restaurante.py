class Restaurante:
    """
    Clase de sercio encargada de administarr 
    los productos del restauraante
    """
    def __init__(self):
        self.productos = []
#Productos 
    def registrar_producto(self, producto):
        self.productos.append(producto)
        print(f"{producto.nombre} Registrado correctamente")

    def mostrar_productos(self):
        print("\n---PRODUCTOS DEL RESTAURANTE---")
        if not self.productos:
            producto("No existen productos registrados")
        
        for producto in self.productos:
            producto.mostrar_informacion()