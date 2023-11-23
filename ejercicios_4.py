#1
"""def Sumar(num1,num2):
    resultado = num1 + num2
    return resultado

print("Ingrese los dos numeros que decea sumar:")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))

print(f"El resultado de la suma es {sumar(num1,num2)}")"""

#2
"""def Saludos(nombre):
    return print(f"Hola {nombre}, Buenos dias!")

nombre = input("Cual es tu nombre?\n=> ")
saludos(nombre)"""

#3

"""def inverti_Cadena(cadena):
    oracion_div = oracion.split(" ")
    al_reves = ""
    oracion_reves = ""
    for x in range(len(oracion_div)):
        for i in oracion_div[x]:
            al_reves = i + al_reves
        oracion_reves = oracion_reves + " " + al_reves
        al_reves = ""
    return print(oracion_reves)


oracion = input("Ingrese una oracion: ")
inverti_cadena(oracion)"""

#4
"""def es_Capicua(numero):
    num_reves = ""
    validar = False
    for x in range(len(numero)):
        for i in numero[x]:
            num_reves = i + num_reves
    
    if numero == num_reves:
        validar = True
    return validar

num = input("Ingrese una numero para ver si es capicua: ")
print(es_capicua(num))"""

#5
"""dudoso"""

#6
"""def es_Par(numero):
    resto = numero % 2
    if resto == 0:
        print(f"el numero {numero} es par")
    else:
        print(f"el numero {numero} es impar")

num = int(input("Ingrece un numero para verificar si es Par o Impar:\n=>"))
es_par(num)"""

#7
"""def imprimir_Pares(numero):
    numeros = ""
    for i in range(1,numero + 1):
        resto = i % 2
        if resto == 0:
            numeros = numeros + f"{i} "
    return numeros

num = int(input("Ingrese un numero: "))
print(imprimir_pares(num))"""

#8
"""def es_Palindromo(palabra):
    al_reves = ""
    for i in palabra:
        al_reves = i + al_reves
    if palabra == al_reves:
        print(f'La palabra "{palabra}" es un palindromo.')
    else:
        print(f'La palabra "{palabra}" no es un palindromo.')

pal = input("ingresa una palabra:\n=>")
es_palindromo(pal)"""

#9
"""def Promedio(numeros):
    suma = 0
    for i in numeros:
        suma += int(i)
    promedio = int(suma / len(numeros))
    return promedio

numeros = (input("ingrese una lista de numeros:\n=>")).split(",")
print(f"el Promedio es de: {Promedio(numeros)}")"""

#10
"""def calcular_factorial(numero):
    factorial = 1
    for i in range(2,numero+1):
        producto = factorial * i
        factorial = producto
    return factorial

num = int(input("ingrese un numero para factirisarlo: "))
print(calcular_factorial(num))
"""

#11
"""def contar_vocales(cadena):
    cont = 0
    for i in cadena.lower():
        if i in "aeiou":
            cont += 1
    return cont

cadena = input("ingrese una oracion o palabra para contar sus vocales: ")
print(f"La canticad de vocales que tiene son: {contar_vocales(cadena)}")"""
#12
"""def convertir_temperatura(celcius):
    fahrenheit= (celcius * (9/5)) + 32
    return fahrenheit

celcius = int(input("ingrese la temperatura en celcius: "))
print(f"{celcius}°C son {convertir_temperatura(celcius):.1f}°F")"""

#17
"""def es_anagrama(palabra1,palabra2):
    anagrama = True
    for i in palabra1:
        if i not in palabra2:
            anagrama = False
            break
    return anagrama

pal1 = input("Ingrese una palabra: ")
pal2 = input("Ingrese una palabra: ")
print(es_anagrama(pal1,pal2))"""
#18
"""def calcular_mayor_diferencia(listnum):
    listnum.sort()
    min_max = []
    min_max.append(listnum[0])
    min_max.append(listnum[-1])
    return min_max

lista_de_numeros = input("Ingrese una lista de numeros: ").split(",")
print(f"El numero mas bajo es '{calcular_mayor_diferencia(lista_de_numeros)[0]}' y el mayor es '{calcular_mayor_diferencia(lista_de_numeros)[-1]}'")"""

#19
"""def es_biciesto(año):
    cuatro = año % 4
    cien = año % 100
    cuatro_cientos = año % 400
    if cuatro == 0 and cien != 0:
        print("es biciesto")
    elif cuatro_cientos == 0:
        print("es biciesto")
    else:
        print("no es biciesto")

año = int(input("Ingrese un año: "))
es_biciesto(año)"""