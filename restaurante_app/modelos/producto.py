class Producto:
#Clase padre que representa un producto general del restaurante
    def __init__(self, nombre, precio, disponibilidad):
        self.nombre = nombre
        self.__precio = precio  #Encapsulación
        self.disponibilidad = disponibilidad
    
    def obtener_precio(self):
        return self.__precio
    
    def cambiar_precio(self, nuevo_precio):
        """Cambia el precio del producto verificando que sea mayor a cero"""
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor a 0")

    
    def mostrar_informacion(self):
        """Muestra la información general del producto"""
        print("\n---PRODUCTO----")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.__precio:.2f}")
        print(f"Disponibilidad: {"Sí" if self.disponibilidad else "No"}")