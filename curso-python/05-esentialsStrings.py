print("Hello, World!")
print("Hola, 'Mundo'!")
print("Hola, \"Mundo\"!")

ingles = "i´m learning python"
multilinea = """Esto es un texto
multilinea"""

print(ingles)
print(multilinea)


palabra = "Python"
print(len(palabra)) # Nos devuelve la cantidad de caracteres que tiene la variable palabra

texto = "Python es un lenguaje de programación"
Incluide = "Python" in texto # Nos devuelve True si la palabra está en el texto, de lo contrario nos devuelve False
print(Incluide)
noIncluide = "Java" not in texto # Nos devuelve True si la palabra no está en el texto, de lo contrario nos devuelve False
print(noIncluide)

print(texto.upper()) # Nos devuelve el texto en mayúsculas
print(texto.lower()) # Nos devuelve el texto en minúsculas
print(texto.capitalize()) # Nos devuelve el texto con la primera letra en mayúscula


spacetext = "   Python is my favorite language   "
print(spacetext.strip()) # Nos devuelve el texto sin espacios al inicio y al final
