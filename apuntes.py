import random as re

"""if letra in palabraSecreta:
        letrasCorrectas = letrasCorrectas + letra"""

"""def mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta,palabraCompleta):
    print(IMÁGENES_AHORCADO[len(letrasIncorrectas)])
    print()

    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()


    for i in range(len(palabraSecreta)): # completar los espacios vacíos con las letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            palabraCompleta = palabraCompleta[:i] + palabraSecreta[i] + palabraCompleta[i+1:]
            return palabraCompleta
    for letra in palabraCompleta: # mostrar la palabra secreta con espacios entre cada letra
        print(letra, end=' ')
    print()"""



#se necesita sacar espaciovacia afuera
"""espaciosVacíos = '_' * len(palabraSecreta)
lista= ["hola", "chau", "papa", "pizza"]
palabra_aleatoria = re.choice(lista)
print(palabra_aleatoria)
#facil
pal = re.choice(lista)
letra_pri = pal[0]
letra_ult = pal[-1]
pista = letra_pri + ("_" * (len(pal)-2)) + letra_ult
#normal

i= re.randint(0,len(pal)-1)#indice de letra
letra = pal[i]
pista = espaciosVacíos[:i] + pal[i] + espaciosVacíos[i+1:]"""

#hay que ver la forma de que lapalabracompleta se rellene con la variable espaciosvacios
"""if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento
        palabracorrecta = ""

# Verifica si el jugador ha ganado.
        
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in palabracorrecta: #todas las letras de palabra secreta tienen que estar dentro de la palabra completa
                break
            else:  
                juegoTerminado = palabraSecreta == palabracorrecta #cuando la palabra secreta sea totalmente igual a los espacios vacios, se da como ganado
else:
    letrasIncorrectas = letrasIncorrectas + intento"""






