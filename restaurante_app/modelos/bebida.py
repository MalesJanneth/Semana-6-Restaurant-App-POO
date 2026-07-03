from modelos.producto import Producto

class Bebida(Producto):
    """
    Representa una bebida del restaurante, este hereda los atributos de Producto
    y añade un atributo propio: tamaño
    """
    def __init__(self, nombre, precio, disponibilidad, tamaño):
        super().__init__(nombre, precio, disponibilidad)
        self.tamaño = tamaño
    
    def mostrar_informacion(self):
        """
        Muestra la información de la bebida. Sobreescribe el método 
        de Producto para demostrar polimorfismo
        """
        print("\n---BEBIDA---")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.obtener_precio():.2f}")
        print(f"Disponibilidad: {"Sí" if self.disponibilidad else "No"}")
        print(f"Tamaño: {self.tamaño}")