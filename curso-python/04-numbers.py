x = 1
y = 2.23
z = 2j

print(type(x)) # Nos permite saber el tipo de variable que es
print(type(y))
print(type(z))

positivo = 5
negativo = -5

# Cambiar tipos de datos
xf = float(x) # Convertimos la variable x a float
print(type(xf))

ye = int(y) # Convertimos la variable y a int
print(type(ye))

ze = complex(z) # Convertimos la variable z a complex
print(type(ze))

#Numeros aleatorios
import random
aleatorio = random.randint(1, 10) # Nos devuelve un número aleatorio entre 1 y 10
print(aleatorio)