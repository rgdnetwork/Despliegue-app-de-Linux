import signal
from time import sleep
import os

print("Bienvenido a mi instalador")
sleep(2) 
print("A continuación deberá de elegir un número para instalar el programa deseado en su máquina")
sleep(2)

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('JDK (Java Development Kit)', accion1),
        '2': ('Visual Studio Code', accion2),
        '3': ('Ngrok', accion3),
        '4': ('Docker', accion4),
        '5': ('Salir', salir)
    }

    generar_menu(opciones, '5')


def accion1():
    print('Has elegido la opción 1')
    sleep(2)
    print("Descargando JDK")
    sleep(2)
    os.system("apt update && apt upgrade -y && apt-get install openjdk-17-jdk -y && java --version")


def accion2():
    print('Has elegido la opción 2')
    sleep(2)
    print("Descargando Visual Studio Code")
    sleep(2)
    os.system(list("sudo apt install snapd -y && sudo snap install --classic code"))
    

def accion3():
    print('Has elegido la opción 3')
    sleep(2)
    print("Descargando Ngrok")
    sleep(2)
    os.system(list("sudo apt install snapd -y && snap install ngrok"))


def accion4():
    print('Has elegido la opción 4')
    sleep(2)
    print("Descargando Docker")
    sleep(2)
    os.system("sudo apt install docker.io -y")


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()