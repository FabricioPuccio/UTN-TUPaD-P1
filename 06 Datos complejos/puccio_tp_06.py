#Práctico listas
""" 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4.
Utilizar la función range. """
print("\nActividad 1:")
lista_multiplo_4 = list(range(4, 101, 4))
print(lista_multiplo_4)


""" 2) Crear una lista con cinco elementos (colocar los elementos que más te
 gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos
o bien investigar cómo funciona el indexing con números negativos! """
print("\nActividad 2:")
list_cinco_ele = ["Hola", "paseo", 3.14, 16, False ]
print(f"El penúltimo elemento de la lista es el: {list_cinco_ele[-2]}")


""" 3) Crear una lista vacía, agregar tres palabras con append e imprimir la 
lista resultante por pantalla. Pista: para crear una lista vacía debes colocar
los corchetes sin nada en su interior."""
print("\nActividad 3:")
lista3 = []
lista3.append("Fabricio")
lista3.append("Puccio")
lista3.append("programación")
print(lista3)

""" 4) Reemplazar el segundo y último valor de la lista “animales” con las 
palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por 
pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo
funciona el indexing con números negativos! """
print("\nActividad 4:")
animales = ["perro", "gato", "conejo", "pez"]
animales[-1] = "oso"
animales[-2] = "loro"
print(animales)

""" 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que 
realiza. """
print("\nActividad 5:")
numeros = [8, 15, 2, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#1. Se crea la lista numeros con sus valores entre corchetes.
#2. Se utiliza el método remove() que quita el elemento que recibe por parámetro.
#3. Para pasar el argumento a remove() se utiliza la función max() la cual 
# recibe por parámetro la lista numeros y devuelve el elemento mayor dentro 
# de la lista.
# Se utiliza la función print para mostrar la lista.

""" 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5
en 5 y mostrar por pantalla los dos primeros. """
print("\nActividad 6:")
lista6 = list(range(10,31,5))
print(lista6[0:2])

""" 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos”
por dos nuevos valores cualesquiera. """
print("\nActividad 7:")
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3]="Lancer", "Ranger"
print(autos)

""" 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15
usando append directamente. Imprimir la lista resultante por pantalla. """
print("\nActividad 8:")
dobles = list()
for i in range(5, 16, 5):
    dobles.append(i * 2)
print(dobles)

""" 9) Dada la lista “compras”, cuyos elementos representan los productos
comprados por diferentes clientes: """
print("\nActividad 9:")
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
""" a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla """
compras[2].append("jugo")
compras[1][1] = "fideos"
compras[0].remove("pan")
print(compras)

""" 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los
siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla. """
print("\nActividad 10:")
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)