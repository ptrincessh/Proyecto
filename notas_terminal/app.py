import os

ARCHIVO = "notas.txt"

def agregar_nota():
    nota = input("Escribe tu nota: ")
    with open(ARCHIVO, "a") as f:
        f.write(nota + "\n")
    print("Nota guardada.")

def ver_notas():
    if not os.path.exists(ARCHIVO):
        print("No hay notas aún.")
        return
    with open(ARCHIVO, "r") as f:
        print("\n--- Tus Notas ---")
        print(f.read())

def borrar_notas():
    if os.path.exists(ARCHIVO):
        os.remove(ARCHIVO)
        print("Notas eliminadas.")
    else:
        print("No hay notas para borrar.")

def menu():
    while True:
        print("\n1. Agregar nota")
        print("2. Ver notas")
        print("3. Borrar notas")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_nota()
        elif opcion == "2":
            ver_notas()
        elif opcion == "3":
            borrar_notas()
        elif opcion == "4":
            print("Adiós")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
