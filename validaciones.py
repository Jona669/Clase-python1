juegos={
    1:{"nombre": "Metroid Dread",
        "precio": 5500,
        "code": "MtDr2022"},
    2:{"nombre": "Zelda TOTK",
        "precio": 5500,
        "code": "zdTk2025"},
}

# print(juegos)

def mostrar_juegos(dict):
    for j,dato in dict.items():
        print(j,dato)

# mostrar_juegos(juegos)
# juegos[3]={"nombre":" SKN VS Capcom 2", "precio":100000, "code": "SKcp2002"}
# mostrar_juegos(juegos)
def valida_nombre(nom):
    for l in nom:
        if " " ==l:
            return True



def valida_precio(p):
    if p>=8000 and p<=100000:
        return True
    else:
        return False


def valida_pass(clave):
    Mayuscula=0
    Minuscula=0
    Numero=0
    for palabra in clave:
        if palabra.isupper():
            Mayuscula+=1
        if palabra.islower():
            Minuscula+=1
        if palabra.isdigit():
            Numero+=1
    if Mayuscula==2 and Minuscula==2 and Numero==4 :
        print("la clave está bien escrita")
        return True
    else:
        print("la clave está mal escrita")
        return False
    

def instertar_juego(dict):
    mostrar_juegos(juegos)
    while True:
        nombre=input("Ingrese el nombre ")
        if valida_nombre(nombre):
            break
        else:
            print("El nombre debe tener dos palabras")
            
    while True:
        precio=int(input("Ingrese el precio "))
        if valida_precio(precio):
            break
        else:
            print("el precio debe estar entre 8000$ y 100000$")
            
    while True:
            codigo=input("Ingrese el codigo ")
            if valida_pass(codigo):
                pos=list(dict.keys())[-1]
                dict[pos+1]={"nombre": nombre, "precio": precio, "code": codigo}
                break
            else:
                    print("el parametro del codigo no es correcto")
                    print("""
                        el codigo debe tener, dos mayusculas, dos minusculas, y cuatro numeros
                        """)

"""el precio debe estar entre $8000 y $100000"""
"""el nombre debe tener por lo menos 2 palabras"""
"""El codigo del juego debe tener 2 mayusculas, 2 minusculas, y cuatro numeros"""

def borrar_juegos(dict):
    mostrar_juegos
    borrar=int(input("Que juego desea borrar "))
    del juegos[borrar]

def actualizar_juegos(dict):
    mostrar_juegos(dict)
    act=int(input("Ingrese el "))
# def actualizar_juegos(dict):

# mostrar_juegos(juegos)
# instertar_juego(juegos)

while True:
    print("""
          1.-registrar juego
          2.-mostrar juego
          3.-actualizar juego
          4.-borrar juego
          5.-salir
          """)
    op=int(input("Elija una opcion "))
    match op:
        case 1:
            instertar_juego(juegos)
        case 2:
            mostrar_juegos(juegos)
        case 4:
            borrar_juegos(juegos)
        case 5:
            print("saliendo")
            break
