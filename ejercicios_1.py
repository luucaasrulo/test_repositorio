#8
"""r = int(input("Ingrese el radio del circulo: "))
pi = 3.1416
diametro = (r * 2)
circ = (diametro * pi)
area = (pi * r**2)
print(f"El diametro es de: {diametro}\nLa circunferencia es de: {circ}\nEl area es de: {area} ")"""
#10
"""dolar = int(input("Cuantos dolares tiene: "))
conversion = dolar * 0.84
print(f"serian {conversion} euros")"""
#11
"""palabra = input("Ingrese palabra: ")
print(len(palabra))"""
#12
"""import re
fecha = re.split("/",input("Ingrese su fecha de Nacimiento\ndd/mm/aaaa\n=> "))
año = int(2023 - int(fecha[2]))
print(f"tenes: {año}Años")"""
#13
"""edad = int(input("Cual es tu Edad:\n=> "))
futuro = edad + 10
print(f"En 10 años va a tener: {futuro}")"""
#14
"""num = int(input("Ingrese un Numero: "))
doble = num * 2
triple = num * 3
print(f"El doble es: {doble}\nY el triple es: {triple}")"""
#15
"""celsius = float(input("Ingrese los grados Celsius: "))
fahren = (celsius * 1.8) + 32
print(f"La convercion a Fahrenheit es: {fahren}°F")"""
#16
"""peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("ingrese si altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu Indice de Masa Corporales de : {imc}")"""
#17
"""import re
palabra = re.split(" ",input("Ingrese dos palabras:\n=> "))
print(palabra[1] + " " + palabra[0])"""
#17.5
"""palabra1 = (input("Ingrese la primer palabra:\n=> "))
palabra2 = (input("Ingrese la segunda palabra:\n=> "))

print(palabra2 + " " + palabra1)"""
#18
"""nombre = (input("Ingrese su Nombre:\n=> "))
edad = (input("Ingrese su Edad:\n=> "))
residencia = (input("Ingrese su lugar de residencia:\n=> "))
print(f"Informacion ingresada\nNombre: {nombre}\nEdad: {edad}\nLugar de residencia: {residencia}")"""
#18.5
"""datos = [input("Ingrese su Nombre:\n=> "),input("Ingrese su Edad:\n=> "),input("Ingrese su lugar de residencia:\n=> ")]
nombre,edad,residencia = datos
print(f"Informacion ingresada\nNombre: {nombre}\nEdad: {edad}\nLugar de residencia: {residencia}")"""
#19
"""number = float(input("ingrese un numero con decimales:\n=> "))
entero = int(number)
decimales = round((number - entero),10)
print(f"Enteros: {entero}\nDecimales: {decimales}")"""



