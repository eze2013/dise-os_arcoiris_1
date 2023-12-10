from os import system   
system("cls")
import sqlite3

def menu():
    print ("DISEÑOS ARCOIRIS" .center(60,"*"))
    print("[1] Agregar producto")
    print("[2] Consultar producto")
    print("[3] Eliminar producto")
    print("[4] Modificar precio Producto")
    print("[5] Modificar un producto en su totalidad")
    print("[6] Listar productos")
    print("[7] Registrar cliente")
    print("[8] Registrar compra del cliente")
    print("[9] Registrar proveedor")
    print("[10] Listar proveedores")
    print("[0] Salir \n")
    opcion=int(input("Ingrese una opcion: "))
    return opcion

def agregar_producto():
    None

def consultar_producto():
    None

def eliminar_producto():
    None
    
def modificar_precio_producto():
    None
    
def main():
    
    opcion=menu()
    while opcion!=0:
        if opcion==1:
          None
        else:
            print("Opcion incorrecta")
        opcion=menu()
    return 

main()