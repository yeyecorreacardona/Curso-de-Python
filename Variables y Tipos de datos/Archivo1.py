"""
Comentarios en Python

"""

# Variables y Tipos de datos

"""
En Python, una variable es un nombre que se utiliza para referirse a un valor almacenado en la memoria.
No es necesario declarar el tipo de dato de una variable antes de usarla, ya que Python es un lenguaje de tipado dinámico.
Los tipos de datos más comunes en Python son:
- int: números enteros  (positivos y negativos) """


"""
variables en python
"""

nombre = "Juan"  # Tipo de dato str (cadena de texto)
edad = 25        # Tipo de dato int (entero)

print("mi edad es" + str(edad))


"""
Como nombrar variables

"""

#no debe tener espacios
#no puede empezar con un numero
#no puede tener caracteres especiales

# no usar nombre poco descriptivos por ejemplo x o dato1

# usar nombres descriptivos por ejemplo

#snake_case
nombre_usuario = "Juan"
edad_usuario = 25

#pascalCase
NombreUsuario = "Juan"
EdadUsuario = 25

#camelCase
nombreUsuario = "Juan"


"""
Uso de la funcion print()

"""

nombre = "Ana"
edad = 30

print("Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años.")
#fstring
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")



"""
Alcance de las variables (scope)

"""
mensaje = "Hola desde el ámbito global"

def saludar():
    mensaje = "Hola desde la función"
    print(mensaje)

saludar()
print(mensaje)
 







