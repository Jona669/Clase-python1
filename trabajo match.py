# pas=1112
# clave=int(input("ingrese su clave"))

# if clave!=pas:
#     print("acceso denegado")
# else:
#     print("acceso permitido")

# def suma():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print("EL resultado de la suma es", n1+n2)
# def resta():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print("EL resultado de la resta es", n1-n2)
# def multi():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print("EL resultado de la multiplicacion es", n1*n2)
# def division(): 
#     try:
#         n1=int(input("Ingrese un numero: "))
#         n2=int(input("Ingrese otro numero: "))
#         print("EL resultado de la resdivisionta es", n1/n2)
#     except ZeroDivisionError as nombre_de_excepcion:
#         # Código para manejar la excepción
#         print(f"Se produjo una excepción: {nombre_de_excepcion}")



# while True:
#     print('''
#         1.- Suma
#         2.- Resta
#         3.- Multiplicacion
#         4.- Division
#         5.-Salir
#         ''')
#     op=int(input("Seleccione un a opcion"))

#     match op:
#         case 1:
#             print("Suma")
#             suma()
#         case 2:
#             print("Resta")
#             resta()
#         case 3:
#             print("Multiplicacion")
#             multi()
#         case 4:
#             print("Division")
#             division()
#         case 5:
#             print("Saliendo")
#             break
#         case _:
#             print("Opcion no valida")

nombre=input("Ingrese su nombre ")
print("Bienvenido/a al sistema ", nombre)
precio=0
lechuga=0
zanahoria=0
repollo=0
huachalomo=0
lomo_liso=0
jamon=0
queso_fresco=0
queso_laminado=0
queso_chanco=0
litro=0
litroymedio=0
treslitros=0
def verd():
    while True:
        print("""
            1.-Lechuga 500$
            2.-Zanahoria 200$
            3.-Repollo 1000$
            4.-Salir""")
        op1=int(input("Seleccione verduras que va a llevar "))
        match op1:
            case 1:
                print("usted agrego una lechuga por 500$")
                precio+500
                lechuga+1
            case 2: 
                print("usted agrego uuna zanahoria por 200$")
                precio+200
                zanahoria+1
            case 3:
                print("usted agrego un repollo por 1000$")
                precio+1000
                repollo+1
            case 4:
                print("SALIENDO AL MENU")
                break

def carne():
    while True:
        print("""
            1.-Huachalomo 5000$
            2.-Lomo liso 7500$
            3.-Jamon 2500$
            4.-Salir""")
        op2=int(input("Seleccione carnes que va a llevar "))
        match op2:
            case 1:
                print("usted agrego huachalomo por 5000$")
                precio+5000
                huachalomo+1
            case 2: 
                print("usted agrego lomo liso por 7500$")
                precio+7500
                lomo_liso+1
            case 3:
                print("usted agrego un jamon por 2500$")
                precio+2500
                jamon+1
            case 4:
                print("SALIENDO AL MENU")
                break

def quesos():
    while True:
        print("""
            1.-Queso fresco 1500$
            2.-Queso laminado 4500$
            3.-Queso chanco 3000$
            4.-Salir""")
        op3=int(input("Seleccione quesos que va a llevar "))
        match op3:
            case 1:
                print("usted agrego Queso fresco 1500$")
                precio+1500
                queso_fresco+1
            case 2: 
                print("usted agrego queso laminado 4500$")
                precio+4500
                queso_laminado+1
            case 3:
                print("usted agrego queso chanco 3000$")
                precio+3000
                queso_chanco+1
            case 4:
                print("SALIENDO AL MENU")
                break

def bebestible():
    while True:
        print("""
            1.-1 litro 1000$
            2.-1.5 litros 1200$
            3.-3 litros 3000$
            4.-Salir""")
        op4=int(input("Seleccione bebidas que va a llevar "))
        match op4:
            case 1:
                print("usted agrego un litro 1000$")
                precio+1000
                litro+1
            case 2: 
                print("usted agrego 1.5 litros 1200$")
                precio+1200
                litroymedio+1
            case 3:
                print("usted agrego 3.0 litros 3000$")
                precio+3000
                treslitros+1
            case 4:
                print("SALIENDO AL MENU")
                break
            case _:
                print("Opcion invalida")

while True:
    print('''
        1.- Verduras
        2.- Carne
        3.- Queso
        4.- Bebestibles
        5.- Salir
        ''')
    op=int(input("Seleccione un a opcion"))
    
    match op:
        case 1:
            print("Verduras")
            verd()
        case 2:
            print("Carne")
            carne()
        case 3:
            print("Queso")
            quesos()
        case 4:
            print("Bebestibles")
            bebestible()
        case 5:
            print("Imprimiendo boleta")
            break

print("el valor total de lo comprado es ", precio)