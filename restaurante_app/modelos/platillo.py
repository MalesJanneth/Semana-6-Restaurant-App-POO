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
        super().mostrar_informacion()
        print(f"Calorías: {self.calorias}")