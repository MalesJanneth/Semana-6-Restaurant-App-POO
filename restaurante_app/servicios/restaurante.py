class Restaurante:
    """
    Clase de sercio encargada de administarr 
    los productos del restauraante
    """
    def __init__(self):
        self.productos = []
#Productos
    def registrar_platillo(self, platillo):
        self.productos.append(platillo)
        print(f"{platillo.nombre} Registrado correctamente")

    def registrar_bebida(self, bebida):
        self.productos.append(bebida)
        print(f"{bebida.nombre} Registrada correctamente")

    def mostrar_productos(self):
        print("\n---PRODUCTOS DEL RESTAURANTE---")
        if not self.productos:
            print("No existen productos registrados")
            return
        
        for producto in self.productos:
            producto.mostrar_informacion()