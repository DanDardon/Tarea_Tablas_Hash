def generar_tabla_hash(texto):
    tabla_hash = {}

    lineas = texto.splitlines()
    for fila, linea in enumerate(lineas):
        palabras = linea.split()
        for columna, palabra in enumerate(palabras):
            if palabra not in tabla_hash:
                tabla_hash[palabra] = []
            tabla_hash[palabra].append((fila, columna))

    return tabla_hash


def imprimir_tabla_hash(tabla_hash):
    print("Tabla Hash:")
    print("-----------")
    for palabra, ubicaciones in tabla_hash.items():
        print(f'{palabra}:')
        for ubicacion in ubicaciones:
            print(f'  Fila: {ubicacion[0]}, Columna: {ubicacion[1]}')
        print("-----------")


def buscar_token(tabla_hash):
    token = input("Ingrese el token a buscar: ")
    if token in tabla_hash:
        ubicaciones = tabla_hash[token]
        print(f'El token "{token}" se encuentra en las siguientes ubicaciones:')
        for ubicacion in ubicaciones:
            print(f'  Fila: {ubicacion[0]}, Columna: {ubicacion[1]}')
    else:
        print(f'El token "{token}" no se encontró en la tabla hash.')


def main():
    print("Programa de Tabla Hash para Código C++")
    print("-------------------------------------")

    print("Ingresa el código C++ (presiona Enter dos veces para finalizar):")
    codigo_c = []
    while True:
        linea = input()
        if not linea:
            break
        codigo_c.append(linea)
    codigo_c = '\n'.join(codigo_c)

    tabla_hash = generar_tabla_hash(codigo_c)

    imprimir_tabla_hash(tabla_hash)

    opcion = input("¿Deseas buscar un token específico? (S/N): ")
    if opcion.upper() == "S":
        buscar_token(tabla_hash)


if __name__ == '__main__':
    main()
