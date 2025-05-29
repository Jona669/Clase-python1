
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

#libreria moda
#crear menu de comics
#1.- Comprar
#2.- Generar boleta
#3.- Salir
#en la opcion de disponibles, mostrar los comics con sus precios
#cuando se compra mostrar la cantidad de articulos que lleva
#mas el monto y monto mas iva
#si ingres codigo de descuento "IAMBATMAN" obtiene 25% de descuento al valor neto
precio=0
CantA=0
def menu():
    while True:
        print("""
              1.- Spiderman $5500
              2.  Batmam $5500
              3.- Capitan america $4000
              4.- Hulk $3500
              5.- Salir al menu""")
        op1=int(input("Seleccione el comic a agregar"))
        match op:
            case 1:
                print("Usted agrego comic spiderman por 5500$")
                precio+=5500
                cantA+=1
            case 2:
                print("Usted agrego comic batman por 5500$")
                precio+=5500
                cantA+=1
            case 3:
                print("Usted agrego comic capitan america por 4000$")
                precio+=4000
                cantA=+1
            case 4:
                print("Usted agrego comic batman por 3500$")
                precio+=3500
                cantA+=1
            case 5:
                print("Saliendo")
                break

def boleta():
    SI="IAMBATMAN"
    cupon=int(input"tiene cupon de descuento? 1=si 2=no")
    if cupon=1
        prueba=(input"Ingrese su cupon de descuento")
        if prueba=SI:
        
        
        
        print("El valor total es ", precio)
        print("El valor mas IVA es de ", precio*1.19)


while True:
    try:
        op=int(input("""
                 1.-Menu
                 2.-Boleta
                 3. Salir
                 """))
        match op:
            case 1:
                menu()
            case 2:
                boleta()
            case 3:
                print()
                break
            case _:
                print("Opcion invalida")
    
    except Exception:
        print("solo numeros enteros")

