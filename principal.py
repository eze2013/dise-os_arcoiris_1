from os import system   
system("cls")
import sqlite3

def menu():
    print("\n")
    print ("DISEÑOS ARCOIRIS" .center(60,"*"))
    print("[1] Agregar producto")
    print("[2] Consultar producto")
    print("[3] Eliminar producto")
    print("[4] Modificar precio Producto")
    print("[5] Modificar un producto en su totalidad")
    print("[6] Listar productos")
    print("[7] Registrar cliente")
    print("[8] Registrar compras del cliente")
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
    
def registro_cliente():
    conexion = sqlite3.connect("base_diseños_arcoiris")
    cursor = conexion.cursor()
    print ("DISEÑOS ARCOIRIS" .center(60,"*"))
    print()
    print("REGISTROS DE CLIENTES".center(60,"*"))
    print("\n")
    num_cliente = int(input("Escribe el numero de cliente a agregar: ")) 
    nombre_cliente = input("Escribe su nombre: ")
    apellido_cliente = input("Escribe su apellido (opcional): ")
    telefono_cliente = int(input("Escribe su telefono: "))
    cursor.execute("INSERT INTO clientes (numero_cliente,nombre,apellido,telefono)VALUES('{0}','{1}','{2}','{3}')"
                   .format(num_cliente,nombre_cliente,apellido_cliente,telefono_cliente))
    conexion.commit()
    conexion.close()
    print("\n CLIENTE AGREGADO CORRECTAMENTE")


def main():
    
    opcion=menu()
    while opcion!=0:
        if opcion==1:
          None
        elif opcion==7:
            registro_cliente()
        else:
            print("Opcion incorrecta")
        opcion=menu()
    return 

main()