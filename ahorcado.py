
#Proyecto 1 "JUEGO DEL AHORCADO" Grupo 4 comision 4 - B

import random 
AHORCADO = ['''
❤❤❤❤❤❤            
  +---+
  |   |
      |
      |
      |
      |            
=========''', '''
❤❤❤❤❤
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
❤❤❤❤
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
❤❤❤
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
❤❤
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
❤
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def Elegir_Dificultad():#es para elegir una dificultad
    dificultad = int(input("""Elija la Dificultad:\n1. Facil\n2. Normal\n3. Dificil\n=> """))
    return dificultad

def Palabra_AlAzar(dificultad):#es para obtener una palabra aleatoria
    lista_1 = ["cama","loca","peso","luna","rata","huella","olla","remo","lago","orca","rima","lata","paso","rizo","palta"]
    lista_2 = ["organizacion","abejas","albaca","alarma","arañas","ocronimos","anagrama","ascension","autonomos","automovil","aguacate","manzana"]
    palabra = ""
    if dificultad == 3:
        palabra = random.choice(lista_2)
    if dificultad != 3:
        palabra = random.choice(lista_1)
    return palabra

def Dar_Pista(palabra,dificultad,):#es para obtener una pista dependiendo de la dificultad
    pista = ""
    if dificultad == 1:#pista 1 nos da la primer y ultima letra de la palabra
        letra_pri = palabra[0]
        letra_ult = palabra[-1]
        pista = letra_pri + ("_" * (len(palabra)-2)) + letra_ult
    elif dificultad == 2:#pista 2 nos da una sola letra aleatoria
        i= random.randint(0,len(palabra)-1)#indice de letra
        palabraCompleta = "_" * len(palabra)
        pista = palabraCompleta[:i] + palabra[i] + palabraCompleta[i+1:]
    elif dificultad == 3:
        pista = "_" * len(palabra)
    return pista



def Pantalla_Juego(AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta,pista):
    print("-------------------------------")
    print(AHORCADO[len(letrasIncorrectas)])#va cambiando de imagen dependiendo del numero de letras incorrectas
    print()
    

    print("Letras incorrectas:", end=" ")#muestra las letras incorrectas separadas por un espacio
    for i in letrasIncorrectas:
        print(i, end=" ")
    print()
    print("-------------------------------\nAdivina la siguiente palabra: ")

    palabraCompleta = pista

    for i in range(len(palabraSecreta)):# completar los espacios vacíos con las letras correctas
        if palabraSecreta[i] in letrasCorrectas:
            palabraCompleta = palabraCompleta[:i] + palabraSecreta[i] + palabraCompleta[i+1:]


    for i in palabraCompleta: # muestrar la palabra con espacios entre cada letra
        print(i, end=" ")
    print()

def Validar_Letra(letrasProbadas):#es para comprobar que solo ingresen 1 letra
    while True:
        letra = input("Ingrese una letra cualquiera: ").lower()
        if len(letra) != 1:
            print("Introduce una sola letra")
        elif letra in letrasProbadas:
            print("Es letra ya la Probaste, elige otra!")
        elif letra not in "abcdefghijklmnñopqrstuvwxyz":
            print("Igrese una 'LETRA'")
        else:
            return letra
        
def jugar_Nuevo():#sirve para reiniciar el juego o finalizarlo
    return input("¿Quieres jugar de nuevo? (sí o no): ").lower().startswith("s")

print("-------------------\nJUEGO DEL AHORCADO\n-------------------")
dificultad = Elegir_Dificultad()
palabra = Palabra_AlAzar(dificultad)
pista = Dar_Pista(palabra,dificultad)
letrasIncorrectas = ""
contador = ""
letrasCorrectas = pista
finJuego = False


while True:
    Pantalla_Juego(AHORCADO, letrasIncorrectas, letrasCorrectas, palabra,pista)


    letra = Validar_Letra(letrasIncorrectas + letrasCorrectas)#se ingresa una letra y se la valida
    if letra in palabra:
        letrasCorrectas = letrasCorrectas + letra
        contador = contador + letra
        palabraCorrecta = pista
        

        for i in range(len(palabra)):#verifica si ganaste
            if palabra[i] in letrasCorrectas:
                palabraCorrecta = palabraCorrecta[:i] + palabra[i] + palabraCorrecta[i+1:]
                finJuego = palabraCorrecta == palabra
                
        if finJuego:
            print(f"-------------------------------------------------\nFelicitaciones, la palabra es: '{palabra.upper()}', ¡HAS GANADO!\n-------------------------------------------------")
         


    else:
        letrasIncorrectas = letrasIncorrectas + letra

        if len(letrasIncorrectas) == len(AHORCADO) - 1:#verifica si agotaste tus intentos
            Pantalla_Juego(AHORCADO, letrasIncorrectas, letrasCorrectas, palabra,pista)
            print(f"-------------------------------------------------------------------------\n¡Te has quedado sin intentos!\nDespués de {str(len(letrasIncorrectas))} intentos fallidos y {str(len(contador))} aciertos, la palabra era '{palabra}' ")
            finJuego = True

    if finJuego:
        print("-------------------------------------------------")
        if jugar_Nuevo():#si elige jugar de nuevo, se le da un nuevo valor a cada variable
            finJuego = False
            dificultad = Elegir_Dificultad()
            palabra = Palabra_AlAzar(dificultad)
            pista = Dar_Pista(palabra,dificultad)
            letrasIncorrectas = ""
            contador = ""
            letrasCorrectas = pista

        else:
            break





