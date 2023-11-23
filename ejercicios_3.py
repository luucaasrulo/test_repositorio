#1
"""palabra = input("ingrese una palabra: ")

for x in palabra:
    print(x,end=" ")"""

#2
"""cont = 0
total = 0
cant = int(input("ingrese un numero: "))

while cont <= cant:
    total += cont
    print(total)
    cont += 1

print("El total es: ",total)"""

#3
"""total = 0
multip = 0
tabla = int(input("Ingrese el numero de la tabla de Multiplicar: "))

while multip < 10:
    multip += 1
    total = multip * tabla
    print(f"{multip} x {tabla} = {total}")"""

#13
"""print("piramide por asteriscos con while")
cant = int(input("cuantos asteriscos: "))
espa = cant
cont = 0

while cont < cant:
    cont += 2
    print((" " * espa) + ("*" * cont))
    espa -= 1

print("piramide por asteriscos")
cant1 = int(input("cantidad de asteriscos: "))
cont1 = 1

for i in range(1,cant1 + 1):
    print("*" * i)

print("piramide por lineas")
cant = int(input("cuantos lineas: ")) * 2
espa = cant
cont = 0

while cont < cant:
    cont += 2
    print((" " * espa) + ("*" * cont))
    espa -= 1

print("piramide perfecta")
cant = int(input("cuantos asteriscos: ")) 
espa = cant - 1
cont = 0

while cont < cant:
    cont += 1
    print((" " * espa) + ("* " * cont))
    espa -= 1"""

#12
"""numeros =(input("lista de numeros, ceparados por coma:\n=>")).split(",")

def suma(num):
    total = 0
    for i in num:
        total += int(i)
    return total

promedio = int(suma(numeros) / len(numeros))
print(f"El promedio de estos numeros es de: {promedio}")"""
#14
"""cant = int(input("Ingrese un numero: "))
espa = cant - 1
cont = 0
for i in range(1,cant+1):
    cont += 1
    print((" " * espa) + ( f"{i} " * cont))
    espa -= 1"""

#15
"""palabra = input("Ingrese una palabra: ").lower()
diccionario = dict()
for i in palabra:

    if i in diccionario.keys():
        diccionario[i] += 1          
    else:
        diccionario[i] = 1

print("las veces que se repiten estas letras son:")
for x in diccionario.items():
    print(x)"""

#16
"""oracion = input("Ingrese una oracion: ")
oracion_div = oracion.split(" ")
al_reves = ""
oracion_reves = ""
for x in range(len(oracion_div)):
    for i in oracion_div[x]:
        al_reves = i + al_reves
    oracion_reves = oracion_reves + " " + al_reves
    al_reves = ""

print(oracion_reves)"""

#17
"""oracion = input("Ingrese una oracion: ")
oracion_div = oracion.split(" ")
al_reves = ""
for x in oracion_div:
    al_reves = x + " " + al_reves
    

print(al_reves)"""

#18


#19
"""num = int(input("Ingrese un numero: "))
resultado = 0
for i in range(1,num):
    resto = num % i
    if resto == 0:
        resultado += i

if resultado == num:
    print(f"El numero {num} es Perfecto.")
else:
    print(f"El numero {num} no es perfecto.")"""

