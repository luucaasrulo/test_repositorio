import modulos
cuenta = {"nombre":None,"pin":None,"saldo": 500}
control = False

#crear usuario o iniciar secion
print("-------------------------------\nBienvenido al cajero automatico\n-------------------------------")
opcion = int(input("""1. Iniciar secion\n2. Crear una Cuenta\n3. salir\n=> """))
if opcion == 1:
    control = bool(modulos.inicio_secion(cuenta["nombre"],cuenta["pin"],control))

elif opcion == 2:
    modulos.crear_cuenta(cuenta)
    control = bool(modulos.inicio_secion(cuenta["nombre"],cuenta["pin"],control))
    
else: 
    print("-------------------------------\n!Hasta luego¡\n-------------------------------")


#menu de opciones
while control == True:
    print("-------------------------------\nBienvenido al Menu...\n-------------------------------")
    opciones = int(input("Elija una opcion\n1. Consultar saldo\n2.Ingresar dinero\n3.Retirar dinero\n4.salir\n=>"))
    if opciones == 1:
        modulos.consultar_saldo(cuenta["saldo"])
    elif opciones == 2:
        modulos.ingresar_dinero(cuenta)
        modulos.consultar_saldo(cuenta["saldo"])
    elif opciones == 3:
        modulos.retirar_dinero(cuenta)
        modulos.consultar_saldo(cuenta["saldo"])
    elif opciones == 4:
        control = False
        print("-------------------------------\n!Hasta luego¡\n-------------------------------")
    else:
        print("-------------------------------\ncomando invalido...\n-------------------------------")