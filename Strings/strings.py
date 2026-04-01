"""
    Un string es una estructura de datos / Tipo de dato secuencial, utilizada para representar
    caracteres alfanumericos, Funciona como una unidad logica que almacena y manipula datos 
    alfanumericos en memoria, permitiendo operaciones como concatenación, busqueda y extracción.
"""

frase = "Hola mundo"

print(len(frase))
print(frase[0])
print("m" in frase)

# Python generaliza cualquier string
print(type(frase))
print(type(frase[0]))

print(frase.upper())