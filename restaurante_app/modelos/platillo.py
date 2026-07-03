from modelos.producto import Producto

class Platillo(Producto):
    """
    Representa un platillo del restaurante, este hereda los atributos de Producto
    y añade un atributo propio: calorias
    """
    def __init__(self, nombre, precio, disponibilidad, calorias):
        super().__init__(nombre, precio, disponibilidad)
        self.calorias = calorias

    def mostrar_informacion(self):
        """
        Muestra la información del platillo, sobre escribe el método Producto
        para demostrar polimorfismo
        """
        print("\n---PLATILLO---")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.obtener_precio():.2f}")
        print(f"Disponibilidad: {"Sí" if self.disponibilidad else "No"}")
        print(f"Calorías: {self.calorias}")
    