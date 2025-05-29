
# num=int(input("ingrese un numero 55"))



# num1=int(input("ingrese otro numero "))



# print(f"la multiplicacion de los numeros es {num*num1}")
# print("Escriba su edad")
# edad=int(input( ))
# if edad>=18:
#     print("usted es mayor de edad")
# else: print("usted no es mayor de edad")


# print("Ingrese su edad")
# edad=int(input())
# if edad<12:
#     print("usted es niño")
# elif edad>=12 and edad<=18:
#     print("usted es adolescente")
# elif edad>18 and edad<65:
#     print("usted es adulto")
# else: print("usted es adulto mayor")


# clave=1234
# print("Ingrese la clave")
# pas=int(input( ))
# if pas==clave:
#       print("Clave correcta")
# else: 
#      print("Clave incorrecta, ingresela nuevamente")


# num=int(input("Ingrese un numero"))

# if num % 2==0:
#     print("El numero es par")
# else:
#     print("El numero es impar")

# color=input("Ingrese un color")

#si es azul es de la u
#si es blanco cc
#si es rojo union
#si es verde audax
#si es otro, color no valido

# if color =="azul":
#     print("es de la u")
# elif color =="blanco":
#     print("es de colo colo")
# elif color =="rojo":
#     print("es de union española")
# elif color =="verde":
#     print("es de audax")
# else: print("color invalido")


#atletas de salto alto
#ingrese cantidad de atletas que paticiparan
#cada atletadebe hacer un alto alto en el rango de 1.55 mt y 3.78 mt
# los atletas bajo 1.55 no califican entre 1.56 y 2 bronce, entre 2.1 y 3 plata, entre 3.1 y mas oro
#poner la altura maxima lograda

atle=int(input("ingrese la cantidad de atletas: "))
record=0
import random

for atleta in range(atle):
    salto=round (random.uniform(1, 3.78), 2)
    if salto>record:
        record=salto
    print(f"El atleta {atleta+1} salto {salto} mts")

    if salto<=1.55:
        print("No clasefica")
    elif salto>=1.56 and salto<=2.0:
        print("A ganado el bronce")
    elif salto>=2.1 and salto<=3.0:
        print("A ganado la plata")
    else:
        print("A ganado el oro")
    print("El record acual es ", record)