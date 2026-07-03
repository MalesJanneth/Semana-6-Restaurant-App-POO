# Sistema Restaurante-App

## Nombre del estudiante
Males Conejo Janneth Talía

---

## Descripción
Este proyecto desarrolla un sistema básico de gestión de productos de un restaurante utilizando Programación Orientada a Objetos en Python.

---

## Estructura del proyecto
```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```
---

## Principios POO aplicados

### Relación de herencia
La clase **Producto** es la clase padre del sistema. Las clases **Platillo** y **Bebida** heredan sus atributos y métodos mediante el uso de `super()` reutilizando el cógigo común y agragando caracteristicas propias de cada producto.

### Encapsulación
El atributo **`__precio`** está encapsulado en la clase Producto. Su acceso y modificación se realiza mediante los métodos:
-`obtener_precio()`
-`cambiar_preci0()`
El método `cambiar_precio()` valida que el nuevo precio sea mayor que 0 antes de actualizarlo.

---

### Polimorfismo
El método `mostrar_informacion()` se sobrescribe en `Platillo` y `Bebida`. Al recorrer la lista de productos en clase `Restaurante`, cada objeto ejecuta su propia versión del método, lo que demuestra el polimorfismo.

---

## Ejecución
Ejecutar desde:


python restaurante_app/main.py


---

## Funcionalidad
- Registrar platillos
- Registrar bebidas
- Cambiar el precio mediante encapsulación
- Mostrar la información de todos los productos utilizando polimorfismo. 

## Reflexión 
La aplicación de los principios de Programación Orientada a Objetos permite desarrollar programas más organizados, reutilizables y fáciles de mantener.
La herencia evita la duplicación de código, la encapsulación protege la información importante y el polimorfismo facilita que diferentes objetos respondan de forma específica a un mismo método.