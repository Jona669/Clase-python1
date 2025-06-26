# # es un conjunto de pares de datos

# dic={
#     "nombre": "Hideo Kojima",
#     "numero": 978789898,
#     "casado": False
# }

# print(dic)

# dic["ciudad"]="Chiloe"

# print(dic)

# for llave, valor in dic.items():
#     print(llave, valor)

# frutas={
#      "manzana": 1200,
#      "melon": 2000,
#      "piña" :3000
#  }

# frutas["durazno"]=2500

# print(frutas)

# nom=input("ingrese el nombre frutas: ")
# valor=int(input("ingrese el valor frutas: "))

# frutas[nom]=valor

# print(frutas)


# while True:
#     try:
#         print("""
#               1.-Ingresar fruta
#               2.-Mostrar fruta
#               3.-Actualizar precio
#               4.-Eliminar fruta
#               5.-Salir
#               """)
#         op=int(input("seleccione una opcion "))
        
#         match op:
#             case 1:
#                 fruta=input("Ingrese el nombre de la fruta ")
#                 precio=int(input("Ingrese el precio "))
#                 frutas[fruta]=precio
#             case 2:
#                 for key,dato in frutas.items():
#                     print(key, "$", dato)
#             case 3:
#                 for key,dato in frutas.items():
#                     print(key, "$", dato)
#                 fru=input("Seleccione la fruta cuyo precio actualizara ")
#                 precio=int(input("Ingrese el precio nuevo "))
#                 frutas[fru]=precio
#             case 4:
#                 for key,dato in frutas.items():
#                     print(key, "$", dato)
#                 borrar=input("Que fruta desea borrar ")
#                 del frutas[borrar]
#             case 5:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("Opcion no valida")
#     except Exception:
#         print("Solo numeros enteros")

# productos=[
#     {"nombre":"lapiz", "precio" : 400},
#     {"nombre":"goma", "precio" : 200},
#     {"nombre":"estuche", "precio" : 1600}
# ]
# print(productos{2})

# tarea
# agregar articulo
# borrar articulo
# actualizar articulo
# mostrar listado de articulos
# salir
# como diccionario


