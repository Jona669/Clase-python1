#uso y ejemplos de listas
#         -5 -4 -3 -2  -1
#numeros=[10, 5, 9, 3, 20]
#          0  1  2  3  4

#print(numeros)
#numeros.reverse()
#for numero in numeros:
 #   print(numero)

#con esto se ve la lista de 2 formas diferentes, con el for, que se repitiria hacia abajo y solamente horizontal

#numeros=[10, 5, 9, 3, 20]
#print(numeros)
#numeros.append(64)
#print(numeros)


#frutas=["durazno", "Naranaja", "Manzana", "Pera"]

#for fruta in frutas:
#    print(fruta)

nombres=["Steven", "George"]
apellidos=["Pal", "Sali"]
while True:
    print("""
          1.- Ingresa un nombre y apellida
          2.- Buscar nombre
          3.- Mostrar nombres y apellidos
          4.- Salir
          """)
    
    op=int(input("Seleccione una opcion "))
    match op:
        case 1:
            persona=input("Ingrese un nombre ")
            apellido=input("Ingrese su apellido ")
            apellidos.append(apellido)
            nombres.append(persona)
            print(len(nombres))
        case 2:
            buscar=input("Que nombre desea buscar? ")
            if buscar in nombres:
                print(f"El nombre {buscar} si existe")
            else:
                print(f"El nombre {buscar} NO existe")
        case 3:
            #c=0
            #for nom in nombres:
                #print(nombres[c], apellidos[c])
                #c+=1
            for i in range(len(nombres)):
                print(nombres[i], apellidos[i])
        case 4:
            print("Saliendo")
            break
        case _:
             print("Ingrese opcion invalida")

#Selecciona una opcion
#Agregar producto (nombre del producto y precio)
#comprar (submenu mostrando producto y precios)
#Crear boleta
#Slir

productos=["Tarjeta Grafica", "Disco SSD", "Procesador"]
precios=["300000", "40000", "150000"]
carrito=[]
cantp=0

while True:
    print("""
          1.-Agregar un producto
          2.-Comprar
          3.-Crear boleta
          4.-Salir
          """)
    
    op=int(input("Seleccione una opcion"))

    match op:
        case 1:
            Agrego=input("Que producto desea agregar?")
            productos.append(Agrego)
        case 2:

        case 3:

        case 4:
            print("Saliendo")
            break
        case _:
            print("Seleccione una opcion valida")