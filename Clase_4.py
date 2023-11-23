#clase de estructura de control de flujo: repetitivos

# uso del WHILF
"""cont = 0
total = 0

entrada = int(input("ingrese cuantas vese se va a repetir: "))

while cont <= entrada:
    total += cont
    print("cont = ", cont)
    print("total = ", total)
    cont += 1

print("finalizo")
print(f"Total: {total}\nCont: {cont}\nSe repitio: {entrada}")"""

#bandera
"""bandera = True
nombres = []
while bandera:
    nombre = input("Ingresa los nombres, y para terminar coloquer 'fin':\n")
    if nombre.lower() != 'fin':
        nombres.append(nombre)
        print(nombres)
    else:
        print("El programa se finalizo correctamente")
        break"""

#uso del FOR

"""lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for num in lista:
    print(num)
"""
#range(start,stop,step)
"""for i in range(0,21,2):
    print(i)
print("fin")"""

#sep= end=
"""for i in range(1):
    print("hola", "asdasd", sep=".", end="___\n")

for i in range(1):
    print("hola", "asdasd", sep="_", edn= ".\n")"""

#Break
"""for x in "Villava":
    if x == "a":
        break
    print(x)"""

