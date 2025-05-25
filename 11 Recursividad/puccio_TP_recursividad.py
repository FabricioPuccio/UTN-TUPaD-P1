# Ejercicios

""" 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
función para calcular y mostrar en pantalla el factorial de todos los números enteros 
entre 1 y el número que indique el usuario """

def factorial(n):
    if n < 2:
        return n
    else:
        return factorial(n - 1) * n
 
num = int(input("Digite un número entero para calcular su factorial: "))
for i in range(num + 1):
    print(f"{i}! = {factorial(i)}")

""" 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
especifique. """

def fibo(pos):
    if pos < 2:
        return pos
    else:
        return fibo(pos - 1) + fibo(pos - 2)

posicion = int(input("\nIngrese la posición hasta donde quiere ver la serie de fibonacci: "))

for i in range(posicion + 1):
    print(f"El valor de la serie de fibonacci en la posición {i} es: {fibo(i)}")

""" 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1)               
. Prueba esta función en un algoritmo general. """

def cal_pot(base, exp):
    if exp == 0:
        return 1
    else:
       return cal_pot(base, exp - 1) * base

print("\nCalculo de potencias")

for i in range(11):
    print(f"{i} elevado a la {i} = {cal_pot(i, i)}")

"""  4) Crear una función recursiva en Python que reciba un número entero positivo en base 
decimal y devuelva su representación en binario como una cadena de texto. """

def dec_a_bin(dec):
    if dec < 2:
        return str(dec%2)
    else:
        return dec_a_bin(dec//2) + str(dec%2)
entero = int(input("\nDecimal a entero.\nNúmero entero positivo en decimal: "))
binario = dec_a_bin(entero)
print(f"Decimal: {entero} -->  Binario: {binario}")


""" 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
lo es.
 Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed() """

def es_palidromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] == palabra[- 1]:
        return es_palidromo(palabra[1:-1])
    else:
        return False

palabra = input("\n¿Es palindromo?\nIngrese por favor una cadena de texto sin espacios ni tildes: ")

if es_palidromo(palabra):
    print(f"La palabra {palabra} es palindromo")
else:
    print(f"La palabra {palabra} no es palindromo")

""" 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
número entero positivo y devuelva la suma de todos sus dígitos.
 Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5) """

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return suma_digitos(n//10) + n%10

dig = int(input("\nSuma digitos\nIngrese un número entero positivo: "))

print(f"La suma de los dígitos del número {dig} es: {suma_digitos(dig)}")

""" 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
pirámide.
 Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1) """

def contar_bloques(n):
    if n == 1:
        return n
    else:
        return contar_bloques(n - 1) + n
bloq = int(input("\nEste programa le informa la cantidad de bloques necesaria para realizar una pirámide.\nPara esto es necesario que ingrese la cantidad de bloques con los que desea realizar el nivel mas bajo: "))

print(f"Si el nivel mas bajo tine {bloq} bloques, el total que necesita para construir la pirámide es de {contar_bloques(bloq)} bloques.")

""" 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
aparece ese dígito dentro del número.
 Ejemplos:
contar_digito(12233421, 2) → 3 
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0 """

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

ent = int(input("\nContador de digitos.\nIngrese un número entero positivo: "))
dg = int(input("Ingrese un dígito (entre 0 y 9): "))

print(f"\nCantidad de veces que se encuentra el dígito {dg} en el número ingresado: {contar_digito(ent, dg)}")
