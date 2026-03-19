def buscar_notas():
    if not os.path.exists(ARCHIVO):
        print("No hay notas aún.")
        return

    palabra = input("Escribe la palabra a buscar: ").lower()
    encontradas = []

    with open(ARCHIVO, "r") as f:
        for linea in f:
            if palabra in linea.lower():
                encontradas.append(linea.strip())

    if encontradas:
        print("\n--- Resultados ---")
        for nota in encontradas:
            print("- " + nota)
    else:
        print("No se encontraron coincidencias.")