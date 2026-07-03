from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante
    
def main():
    """
    Punto de entrada del programa
    """
    restaurante = Restaurante()
    #Platillos
    platillo1 = Platillo("Arroz con camarón", 5.5, True, "350")
    platillo2 = Platillo("Seco de pollo", 4.0, True, "450")
    #Bebidas
    bebida1 = Bebida("Jugo natural", 1.5, False, "250ml")
    bebida2 = Bebida("Gaseosa", 2.50, True, "330ml")

    restaurante.registrar_producto(platillo1)
    restaurante.registrar_producto(platillo2)
    restaurante.registrar_producto(bebida1)
    restaurante.registrar_producto(bebida2)

    print("\nActualizar el precio de la bebida")
    bebida2.cambiar_precio(2.25)

    restaurante.mostrar_productos()

if __name__ == "__main__":
    main()