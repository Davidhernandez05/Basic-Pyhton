# String
comillasSimples = 'Hola Mundo'
comillasDobles = "Hola Mundo"
comillasTriples = '''Hola Mundo'''

print(comillasSimples)
print(comillasDobles)
print(comillasTriples)

# Numbers
Enteros = 10
Decimales = 3.14
EnterosNegativos = -5
numerosReales = 2.5e2

print(Enteros)
print(Decimales)
print(EnterosNegativos)
print(numerosReales)

#Lists

lista = [1, 2, 3, 4, 5] # La lista es mutable, es decir, podemos modificarla después de haberla creado
print(lista)
lista.append(6) #Agregamos un elemento al final de la lista
print(lista)
lista.remove(3) #Eliminamos el elemento 3 de la lista
print(lista)
print(lista[0]) #Nos devuelve el primer elemento de la lista
print(lista[-1]) #Nos devuelve el último elemento de la lista

#Tuplas
tupla = (1, 2, 3, 4, 5) #La tupla es inmutable, es decir, no podemos modificarla después de haberla creado
print(tupla)
print(tupla[0]) #Nos devuelve el primer elemento de la tupla
print(tupla[-1]) #Nos devuelve el último elemento de la tupla


#Diccionarios
diccionario = {
  "nombre": "David", 
  "edad": 30, 
  "ciudad": "Madrid"
} #El diccionario es mutable, es decir, podemos modificarlo después de haberlo creado

print(diccionario)
print(diccionario["nombre"]) #Nos devuelve el valor de la clave "nombre"
print(diccionario["edad"]) #Nos devuelve el valor de la clave "edad"
print(diccionario["ciudad"]) #Nos devuelve el valor de la clave "ciudad"

#Sets
conjunto = {1, 1, 2, 3, 4, 5} #El conjunto es mutable, es decir, podemos modificarlo después de haberlo creado
print(conjunto)
conjunto.add(6) #Agregamos un elemento al conjunto
print(conjunto)


#Booleanos
verdadero = True
falso = False
print(verdadero)
print(falso)