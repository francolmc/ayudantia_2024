# Cabecera del programa
from DTO.persona import Persona
from DTO.trabajador import Trabajador

# Funcion
def saludar(nombre: str):
    # Cabecera de la funcion
    # Cuerpo de la funcion
    print(f"Hola {nombre}")
    # FIN de la funcion

# Instanciar, proceso de construir un objeto a partir de una clase
# En este ejemplo estamos construyendto a la pedro como una Persona
pedro = Persona()
pedro.edad = 25 # Asignar una edad al atributo edad de Persona
pedro.nombre = "Pedro Rojas" # Asignar un nombre al artibuto nombre de Persona
pedro.caminar()

saludar(pedro.nombre)


angela = Trabajador()
angela.nombre = "Angela Castro"
angela.edad = 34
angela.codigo_trabajador = "123456"
angela.caminar()
angela.trabajar()
