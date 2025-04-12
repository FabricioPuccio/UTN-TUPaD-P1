""" Actividades

1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 
"""


for i in range(101):
    print(i)


""" 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene.
"""


cont = 0
num = input("Hola, por favor ingrese un número entero: ")

for i in num:
    if i != "-":
        cont += 1

print(f"El número: {num} contiene {cont} dígitos.")


""" 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores. 
"""


suma = 0
valor_uno = int(input("Por favor, ingrese el primer valor entero: "))
valor_dos = int(input("Ingrese el segundo valor entero: "))
if valor_uno > valor_dos:
    aux = valor_uno
    valor_uno = valor_dos
    valor_dos = aux

for i in range((valor_uno + 1), valor_dos):
    suma += i

print(f"El resultado de la suma de los números comprendidos entre los dos valores ingresados es: {suma}")    


""" 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0.
"""


sumatoria = 0
numero = int(input("Por favor ingrese un número entero o 0 para terminar: "))
while numero != 0:
    sumatoria += numero
    numero = int(input("Ingrese otro número entero o 0 para terminar: "))

if sumatoria == 0:
    print("Programa finalizado!!!")
else:
    print(f"\nHemos sumado cada número ingresado y el resultado es: {sumatoria}")


""" 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 
"""


import random
num_aleatorio = random.randint(0,9)
intentos = 1
num_correcto = int(input("Veamos en cuantos intentos usted adivina el número escondido." \
"\nIngrese un numero comprendido entre 0 y 9: "))
while num_correcto != num_aleatorio:
    intentos += 1
    num_correcto = int(input("Ingrese otro número comprendido entre 0 y 9: "))

print(f"\nFelicitaciones encontraste el número escondido en {intentos} intentos.")


""" 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente.
""" 


print("Números pares comprendidos entre 0 y 100 en orden decreciente:")
for i in range(100, 1, -2):
    print(i)
   

""" 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario. 
"""


npos = int(input("Vamos a realizar la suma de los números comprendidos entre 0 y el número ingresado.\n" \
"Ingrese un número entero positivo: "))
print("El resultado es: " + str(sum(i for i in range(npos + 1))))


""" 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""


par = 0
impar = 0
neg = 0
pos = 0
for i in range(1, 101):
    num = int(input("Ingrese el "+str(i)+"° número: "))

    if num < 0:
        neg += 1
    else:
        pos += 1

    if num%2 == 0:
        par += 1
    else:
        impar += 1   


print(f"\nNúmeros pares: {par}") 
print(f"Números impares: {impar}") 
print(f"Números negativos: {neg}") 
print(f"Números positivos: {pos}") 


""" 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor). 
"""


from statistics import mean

lista = []

for i in range(100):
    num = int(input("Ingrese, por favor, un número entero: "))
    lista.append(num)

print("La media de los números ingresados es:", mean(lista))


""" 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. """


n_str = input("Este programa invierte el orden de un número\nPor favor ingrese un número entero positivo: ")
l_num = []
for i in n_str:
    l_num.append(i)
l_num.reverse()
for i in l_num:
    print(i, end="")

