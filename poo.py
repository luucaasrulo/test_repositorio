import random 
#Definir clase

class Persona:

    nacionalidad = "Argentina"

    def __init__(self,nombre,apellido,email,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.__email = email
        self.edad = edad
        self.direcion = None

    def __str__(self):
            return (f"Hola {self.nombre} {self.apellido} tu edad es: {self.edad} y tu email es el siguiente: {self.email}")

    def saludar(self):
        print(f"Hola {self.nombre} {self.apellido} tu edad es: {self.edad} y tu email es el siguiente: {self.__email}")

"""persona1 = Persona("Lucas","Villalva", "Lucas___1997", 26)
persona1.saludar()
print(persona1._Persona__email)
"""

"""Ejercicio 8: Mis Libros Favoritos
    Vamos a crear un programa para nuestros libros favoritos. Queremos mantener una lista de los libros que hemos ido leyendo, 
    calificando según nos haya gustado más o menos al leerlo.

        * Para ello, crear la clase Libro, cuyos atributos son el titulo, el autor, 
        el número de páginas y la calificación que le damos entre 0 y 10.

        * Crear los métodos para poder modificar y obtener los atributos si tienen sentido.

        *Posteriormente, crear una clase ConjuntoLibros, que almacena un conjunto de libros.

            ___Se pueden añadir libros que no existan (siempre que haya espacio).
            ___eliminar libros por título o autor. 
            ___mostrar por pantalla los libros con la mayor y menor calificación dada.
            ___por último, mostrar un contenido de todo el conjunto."""

class Libro:

    def __init__(self,autor,titulo,num_pagina):
        self.autor = autor
        self.titulo = titulo
        self.num_pagina = num_pagina
        self._calificacion= None

    def setCalificacion(self,calificacion):
        if calificacion >= 0 and calificacion <= 10:
            self._calificacion = calificacion
        else:
            print("El valor esta fuera de los parametros, tiene que estar entre 0 y 10.")
    
    def getCalificacion(self):
        return self._calificacion

class ConjuntoLiblos:

    def __init__(self,capacidad):
        self.libros = []
        self.capacidad = capacidad
        self.mejor_libro = None
        self.peor_libro = None

    def agregar_libro(self,libro):
        if len(self.libros) < self.capacidad :
            self.libros.append(libro)
            print("El libro fue agregado con exito!")
            if self.peor_libro == None or libro.getCalificacion() < self.peor_libro.getCalificacion():
                self.peor_libro = libro
            if self.mejor_libro == None or libro.getCalificacion() > self.mejor_libro.getCalificacion():
                self.mejor_libro = libro
        else:
            print("No se puedo agregar el libro, su libreria esta llena.")
    
    def getMejorLibro(self):
        return self.mejor_libro
    
    def getPeorLibro(self):
        return self.peor_libro
    
    def eliminar_por_titulo(self,titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                print(f"El libro '{libro.titulo}', fue eliminado de la biblioteca.")
    
    def eliminar_por_autor(self,autor):
        for libro in self.libros:
            if libro.autor == autor:
                self.libros.remove(libro)
                print(f"El libro '{libro.titulo}' del autor '{libro.autor}', fue eliminado de la biblioteca.")

    def mostrar_contenido(self):
        if not self.libros:
            print('No hay libros cargados aun.')
        else:
            for libro in self.libros:
                print(f"Titulo: {libro.titulo}, Autor: {libro.autor}, Calificacion: {libro.getCalificacion()}, Numero de paginas: {libro.num_pagina}")

"""
libro1 = Libro("J. K. Rowling","Harry Potter", 500)
libro1.setCalificacion(7)

libro2 = Libro("Stephen King", "It", 1000)
libro2.setCalificacion(2)

libro3 = Libro("Jorge", "Panaderia", 4839)
libro3.setCalificacion(10)



conjunto_libros = ConjuntoLiblos(5)
conjunto_libros.agregar_libro(libro1)
conjunto_libros.agregar_libro(libro2)
conjunto_libros.agregar_libro(libro3)
print("------------------------------------------")

print(f"el mejor libro es: {conjunto_libros.getMejorLibro().titulo} y su calificacion es: {conjunto_libros.getMejorLibro().getCalificacion()}")
print(f"El peor libro es: {conjunto_libros.getPeorLibro().titulo} y su calificacion es: {conjunto_libros.getPeorLibro().getCalificacion()}")

print("------------------------------------------")

conjunto_libros.mostrar_contenido()
print("------------------------------------------")

conjunto_libros.eliminar_por_titulo("It")
print("------------------------------------------")

conjunto_libros.mostrar_contenido()
print("------------------------------------------")

conjunto_libros.eliminar_por_autor("J. K. Rowling")
print("------------------------------------------")

conjunto_libros.mostrar_contenido()
print("------------------------------------------")"""

"""Ejercicio 4: Tiempo
Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser
instanciada indicando: los tres atributos, sólo la hora y minuto, o sólo la hora.
Crear además los métodos necesarios para modificar la hora en cualquier
momento de forma manual. Mantenga la integridad de los datos en todo
momento definiendo de tipo “private”. Crear una clase prueba_tiempo que
prueba una hora concreta y la modifique a su gusto mostrándola por pantalla."""

class Tiempo:

    def __init__(self,hora = 0,minutos = 0,segundos = 0):
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos

    def setHora(self,hora):
        if 0 <= hora < 24:
            self.__hora = hora
        else:
            print("La hora Ingresada, supera el rango permitido.")
    
    def setMinutos(self,minutos):
        if 0 <= minutos < 60:
            self.__minutos = minutos
        else:
            print("Los minutos ingresados, superan el rango permitido.")

    def setSegundo(self,segundos):
        if 0 <= segundos < 60:
            self.__segundos = segundos
        else:
            print("Los segundos ingresados, superan el rango permitido.")

    def getHora(self):
        return self.__hora
    
    def getMinutos(self):
        return self.__minutos
    
    def getSegundos(self):
        return self.__segundos
    
    def mostrar_hora(self):
        return f"{self.getHora()}:{self.getMinutos()}:{self.getSegundos()}"
    
class PruebaTiempo:

    def __init__(self):
        self.tiempo = Tiempo()

    def prueba_tiempo(self):
        hora = random.randint(0,24)
        minutos = random.randint(0,60)
        segundos = random.randint(0,60)
        self.tiempo.setHora(hora)
        self.tiempo.setMinutos(minutos)
        self.tiempo.setSegundo(segundos)
        print(self.tiempo.mostrar_hora())


"""prueba = PruebaTiempo()

prueba.prueba_tiempo()"""

class CuentaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, monto):
            if monto > 0:
                self._saldo += monto
                print(f"el depocito de {monto} fue realizado con exito.\n Su saldo actual es de {self._saldo}")
            else:
                 print("La cantidad ingresada es menos a 0.")

    def retirar(self,retiro):
        if retiro <= self._saldo:
              self._saldo -= retiro
              print(f"El retiro de {retiro} feu realizado con exito.\n Su saldo actual es de {self._saldo}")
        else:
             print("Saldo insuficiente.")

"""cuenta = CuentaBancaria("Lucas", 100000)
cuenta.depositar(500)
cuenta.retirar(1500)
cuenta.retirar(100000)"""

class Titular:
     
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.__cuil = None
          
    def __getCuil(self):
        return self.__cuil
    
    def __setCuil(self,cuil):
        if 9 < len(cuil) <= 11:
            self.__cuil = cuil    
        else:
              print("El cuil ingresado es incorrecto.")

class Banco:
     
    def __init__(self,nombre):
        self.nombre = nombre
        self.__cuil = None

    def __getCuil(self):
        return self.__cuil
    
    def __setCuil(self,cuil):
        if 9 < len(cuil) <= 11:
             self.__cuil = cuil    
        else:
              print("El cuil ingresado es incorrecto.")
          
class CuentaBancarria(Titular,Banco):
    def __init__(self, nombre_titular, apellido_titular, edad, nombre_banco, saldo =0):
        Titular.__init__(self, nombre_titular, apellido_titular, edad)
        Banco.__init__(self,nombre_banco)
        self._saldo = saldo
     
    def depositar(self, monto):
            if monto > 0:
                self._saldo += monto
                print(f"el depocito de {monto} fue realizado con exito.\n Su saldo actual es de {self._saldo}")
            else:
                print("La cantidad ingresada es menos a 0.")

    def retirar(self,retiro):
        if retiro <= self._saldo:
              self._saldo -= retiro
              print(f"El retiro de {retiro} feu realizado con exito.\n Su saldo actual es de {self._saldo}")
        else:
             print("Saldo insuficiente.")

"""cuenta1 = CuentaBancarria("Lucas", "Villalva", 26, "Hipotecario", 100000)
cuenta1._Titular__setCuil("20400350281")
cuenta1._Banco__setCuil("20400350281")  

print(cuenta1._Titular__getCuil())
print(cuenta1._Banco__getCuil())"""


class Persona:
    def __str__(self):
        return "Hola soy una persona"
    
class Empleado(Persona):
    def __str__(self):
        return super().__str__() + " Y tambien soy un empleado"

"""empleado = Empleado()
print(empleado)"""




"""class Pizza():
    def __init__(self,porcion):
        pass"""