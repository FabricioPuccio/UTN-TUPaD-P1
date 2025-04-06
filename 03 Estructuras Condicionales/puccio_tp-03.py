""" Actividades
1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. """

anio = int(input("Por favor ingrese su edad: ") )
if anio >= 18:
    print("Es mayor de edad")


""" 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”. """

nota = int(input("Ingrese su nota: "))
respuesta = "Aprobado" if (nota >= 6) else "Desaprobado" 
print(respuesta)


""" 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar. """

num = int(input("Hola! Por favor, ingrese un número par: "))

if num % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.") 


""" 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años. """

edad = int(input("Hola, este programa le informa su categoría en relación con su edad.\n"
"Por favor ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


""" 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string. """

passw = input("(Atención la contraseña debe tener entre 8 y 14 caracteres)\nIngrese su contraseña: ")
if len(passw) >= 8 and len(passw) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


""" 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
y calcular la moda, la mediana y la media de dichos números.
En la documentación oficial se puede encontrar más información sobre este paquete:
https://docs.python.org/es/3.8/library/statistics.html.
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
mediana es mayor que la moda.
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
la mediana es menor que la moda.
● Sin sesgo: cuando la media, la mediana y la moda son iguales.
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir una lista numeros_aleatorios. """

import random
from statistics import mode, median, mean
print("Este programa crea una lista de números aleatorios y determina si exite un sesgo e imprime el resultado: ")

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda: 
    print("Sesgo positivo o a la derecha.")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda.")
elif media == mediana and mediana == moda:
    print("Sin sesgo")


""" 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla. """

frase = input("Hola, por favor ingresa una frase o palabra: ")
ult_let = frase[len(frase) - 1].lower()
if ult_let == "a" or ult_let == "e" or ult_let == "i" or ult_let == "o" or ult_let == "u":
    print(frase+"!")
else:
    print(frase)


""" 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas. """ 

name = input("Hola, por favor ingrese su nombre: ")
opc = int(input("Ingrese 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n"
"Ingrese 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n"
"Ingrese 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.\n"
"Opción: "))
if opc == 1:
    print(name.upper())
elif opc == 2:
    print(name.lower())
elif opc == 3:
    print(name.title())
else:
    print("Error, ingresó un dígito invalido!") 


""" 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""

magnitud = float(input("Para conocer la categoría, ingrese la magnitud del terremoto: ")) 
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud >= 7:
    print("Extremo (puede causar daños a gran escala).") 


""" Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano. """

hemisferio = input("\nHola, en cuál hemiferio te encuentras: N (norte) / S (sur): ")
mes = input("¿Qué mes del año es?: ")
dia = int(input("¿Qué día es?: "))

hemisferio = hemisferio.upper()
mes = mes.lower() 

print("")

if dia > 0 and dia <= 31:
    
    if hemisferio == "S":

        if mes == "enero" or (mes == "febrero" and dia <= 28):
            print("Usted se encuentra en la estación de verano.")
        elif (mes == "abril" and dia <= 30) or mes == "mayo":
            print("Usted se encuentra en otoño.")    
        elif mes == "julio" or mes == "agosto":
            print("Usted está en la estación de invierno.")
        elif mes == "octubre" or (mes == "noviembre" and dia <= 30):
            print("La estación donde se encuentra es primavera.")        
        
        if mes == "diciembre" and dia >= 21:
            print("Usted se encuentra en la estación de verano.")
        elif mes == "diciembre" and dia <  21:
            print("La estación donde se encuentra es primavera.")

        if mes == "marzo" and dia >= 21:
            print("Usted se encuentra en otoño.")
        elif mes == "marzo" and dia <  21:
            print("Usted se encuentra en la estación de verano.")

        if mes == "junio" and (dia >= 21 and dia <=30):
            print("Usted está en la estación de invierno.")
        elif mes == "junio" and dia <  21:
            print("Usted se encuentra en otoño.")

        if mes == "septiembre" and (dia >= 21 and dia <=30):
            print("La estación donde se encuentra es primavera.")
        elif mes == "septiembre" and dia <  21:
            print("Usted está en la estación de invierno.")

        if mes == "febrero" and dia > 28:
            print("Error, en el año 2025 Febrero tiene 28 días!")

        if dia > 30 and (mes == "abril" or mes == "noviembre" or mes == "junio" or mes == "septiembre"):
            print(f"Error, el mes de {mes} no tiene {dia} días!")         

    elif hemisferio == "N":
        
        if mes == "enero" or (mes == "febrero" and dia <= 28):
            print("Usted se encuentra en la estación de invierno.")
        elif (mes == "abril" and dia <= 30) or mes == "mayo":
            print("Usted se encuentra en primavera.")
        elif mes == "julio" or mes == "agosto":
            print("Usted está en la estación de verano.")
        elif mes == "octubre" or (mes == "noviembre" and dia <= 30):
            print("La estación donde se encuentra es otoño.")        
        else:
            print("Día ingresado invalido!") 
       
        if mes == "diciembre" and dia >= 21:
            print("Usted se encuentra en la estación de invierno.")
        elif mes == "diciembre" and dia <  21:
            print("La estación donde se encuentra es otoño.")

        if mes == "marzo" and dia >= 21:
            print("Usted se encuentra en primavera.")
        elif mes == "marzo" and dia <  21:
            print("Usted se encuentra en la estación de invierno.")

        if mes == "junio" and (dia >= 21 and dia <=30):
            print("Usted está en la estación de verano.")
        elif mes == "junio" and dia <  21:
            print("Usted se encuentra en primavera.")

        if mes == "septiembre" and (dia >= 21 and dia <=30):
            print("La estación donde se encuentra es otoño.")
        elif mes == "septiembre" and dia <  21:
            print("Usted está en la estación de verano.")

        if mes == "febrero" and dia > 28:
            print("Error, en el año 2025 Febrero tiene 28 días!")

        if dia > 30 and (mes == "abril" or mes == "noviembre" or mes == "junio" or mes == "septiembre"):
            print(f"Error, el mes de {mes} no tiene {dia} días!")

    else:
        print(f"Error, el hemisferio ingresado: {hemisferio}, es incorrecto!")

else:
     print("Día ingresado invalido!")




                      
          






