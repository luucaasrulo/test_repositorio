#inicio de secion
def inicio_secion(nombre,contraseña,control):
    intentos =3
    control = control
    while intentos != 0:
            usuario = str(input("-------------------------------\ningrese su usuario:\n=>"))
            pin = str(input("Ingrese si PIN:\n=>"))
            if usuario == nombre and pin == contraseña:
                control = True
                return control
            else:
                print("-------------------------------\nUsuario o Contraseña incorrecta, vuelve a intentarlo...\n-------------------------------")
                intentos -=1
                print(f"-------------------------------\nLe queda {intentos} intentos.\n-------------------------------")
    return control


#crear_cuenta
def crear_cuenta(x):
     x["nombre"] = str(input("-------------------------------\nIngrese nombre de usuario: "))
     x["pin"] = str(input("Ingrese el PIN: "))
     x["saldo"] = 0.00
     return x

#Menu de opciones
#saldo
def ingresar_dinero(cuenta):
    dinero = int(input("-------------------------------\ncuanto dinero desea ingresar:\n=>"))
    total = cuenta["saldo"] + dinero
    cuenta["saldo"] = total
    return

def retirar_dinero(cuenta):
    dinero = int(input("-------------------------------\ncuanto dinero desea retirar:\n=>"))
    total = cuenta["saldo"] - dinero
    cuenta["saldo"] = total
    return

def consultar_saldo(cuenta):
    print(f"-------------------------------\nTu saldo actual es de: {cuenta}\n-------------------------------")