import random


def clave():
    clave=3344
    password=int(input("Ingrese su pass :"))
    while clave!=password:
        print ("ERORR, clave invalida")
        password=int(input("Ingrese su pass :"))

    print("Bienvenido al sistema")

def ruleta():
    barril=random.randint(1,6)
    rul=int(input("Dispare"))

    while rul!=barril:
        rul=int(input("Dispare"))
    print("BANG!!!")

def suma():
    n1=int(input("Ingrese un numero "))
    n2=int(input("Ingrese otro numero "))
    print("La suma total es", n1+n2)

def suma_arg(n1,n2):
    print(n1+n2)

def suma_ret():
    n1=int(input("Ingrese un numero "))
    n2=int(input("Ingrese otro numero "))
    return n1+n2
def suma_ret_arg(n1,n2):
    return n1+n2
#suma()
#suma_arg(9,5)
#print (suma_ret()*3)
#print(suma_ret_arg(6,9))

def suma_3000(num):
    return num+3000

#result=suma_3000(4000)
#print(result)

def iva(num):
    print("El iva de", num," es =", num*1.19)
# num=int(input("Ingrese la cantidad de la que quiere saber el iva "))
# iva(num)

def iva_ret(num):
    return num*1.19

# result=iva_ret(4000)
# print(result)

def descuento(pre,des):
    return pre-(pre*des/100)

result=descuento(3000,20)
print(result)