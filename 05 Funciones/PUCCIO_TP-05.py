from math import pi, pow
# Definición de funciones
def imprimir_hola_mundo(mensaje):
    print(mensaje)

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")  

def informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def calcular_area_circulo(r):
    return pi * pow(r, 2)

def calcular_perimetro_circulo(r):
    return 2 * pi * r

def segundos_a_horas(segundos):
    horas = segundos // 3600
    segundos = segundos % 3600
    minutos = segundos // 60
    segundos = segundos % 60
    return horas, minutos, segundos

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} * {i} = {numero * i}")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    if a != 0 and b != 0:
        div = a / b
    else:
        div = 0  
    tupla = (suma, resta, mult, div)              
    return tupla   

def calcular_imc(peso, altura):
    return peso / pow(altura, 2)

def celsius_a_fahrenheit(celsius):
    #ºF = (ºC · 1,8) + 32
    return (celsius * 1.8) + 32

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal

""" 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”.
Llamar a esta función desde el programa principal. """
print("\nEjercicio 1")
imprimir_hola_mundo("Hola Mundo!")

""" 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva
un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
Llamar a esta función desde el programa principal solicitando el nombre al usuario. """
print("\nEjercicio 2")
saludar_usuario(input("Ingrese su nombre: "))

""" 3. Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) que reciba cuatro parámetros
e imprima: “Soy[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a 
esta función con los valores ingresados. """
print("\nEjercicio 3")
nom = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nom, apellido, edad, residencia)

""" 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados. """
print("\nEjercicio 4")
radio = float(input("Para conocer el área y el perímetro de un circulo, por favor ingrese su radio: "))
print(f"El área del circulo es: {calcular_area_circulo(radio)}")
print(f"El perímetro del circulo es: {calcular_perimetro_circulo(radio)}")

""" 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro
y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando
esta función. """
print("\nEjercicio 5")
h, m, s = segundos_a_horas(int(input("Por favor ingrese los segundos: ")))
print(f"La cantidad en segundos ingresada equivale a {h} hora/s, {m} minuto/s , {s} segundo/s")  

""" 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y
imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función. """
print("\nEjercicio 6")
num = int(input("Tabla de multiplicar, ingrese un número entero positivo: "))
tabla_multiplicar(num)

""" 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y 
devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
Mostrar los resultados de forma clara. """
print("\nEjercicio 7")
num1 = float(input("Operaciones básicas.\nIngrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma, resta, mult, div = operaciones_basicas(num1, num2)
print(f"{num1} + {num2} =  {suma}")
print(f"{num1} - {num2} =  {resta}")
print(f"{num1} * {num2} =  {mult}")
print(f"{num1} / {num2} =  {div}")

""" 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros,
y devuelva el índice de masa corporal (IMC). 
Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales. """
print("\nEjercicio 8")
peso = float(input("Calculo de masa corporal (IMC).\nIngrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print("Su índice de masa corporal es {:.2f}".format(calcular_imc(peso, altura)))

""" 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función. """
print("\nEjercicio 9")
print("Temperature:")
celsius = float(input("Grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print("Grados Fahrenheit {}".format(fahrenheit))

""" 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función. """
print("\nEjercicio 10")
n_uno = float(input("Promedio de tres números.\nIngrese el primer número: "))
n_dos = float(input("Ingrese el segundo número: "))
n_tres = float(input("Ingrese el tercer número: "))
print(f"El promedio de los núemeros ingresados es: {calcular_promedio(n_uno, n_dos, n_tres)}")




