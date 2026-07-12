def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            print("Debe seleccionar una opcion valida")
        except ValueError:
            print("Debe seleccionar una opcion valida")


def unidades_categoria(categoria, d_prendas, d_bodega):
    total_unidades = 0

    for codigo, datos_prenda in d_prendas.items():
        if datos_prenda[1].lower() == categoria.strip().lower():
            total_unidades += d_bodega[codigo][1]

    print(f"El total de unidades disponibles es: {total_unidades}")


def busqueda_precio(p_min, p_max, d_prendas, d_bodega):
    prendas_encontradas = []

    for codigo, datos_bodega in d_bodega.items():
        precio = datos_bodega[0]
        unidades = datos_bodega[1]

        if p_min <= precio <= p_max and unidades != 0:
            nombre = d_prendas[codigo][0]
            prendas_encontradas.append(f"{nombre}--{codigo}")

    prendas_encontradas.sort()

    if len(prendas_encontradas) > 0:
        print(f"Las prendas encontradas son: {prendas_encontradas}")
    else:
        print("No hay prendas en ese rango de precios.")


def buscar_codigo(codigo, d_prendas):
    codigo_buscado = codigo.strip().upper()

    for codigo_prenda in d_prendas:
        if codigo_prenda.upper() == codigo_buscado:
            return True

    return False


def obtener_codigo_real(codigo, d_prendas):
    codigo_buscado = codigo.strip().upper()

    for codigo_prenda in d_prendas:
        if codigo_prenda.upper() == codigo_buscado:
            return codigo_prenda

    return None


def actualizar_precio(codigo, nuevo_precio, d_prendas, d_bodega):
    if buscar_codigo(codigo, d_prendas):
        codigo_real = obtener_codigo_real(codigo, d_prendas)
        d_bodega[codigo_real][0] = nuevo_precio
        return True

    return False


def validar_codigo(codigo):
    return codigo.strip() != ""


def validar_nombre(nombre):
    return nombre.strip() != ""


def validar_categoria(categoria):
    return categoria.strip() != ""


def validar_talla(talla):
    return talla.strip() != ""


def validar_color(color):
    return color.strip() != ""


def validar_material(material):
    return material.strip() != ""


def validar_es_unisex(es_unisex):
    return es_unisex.strip().lower() == "s" or es_unisex.strip().lower() == "n"


def validar_precio(precio):
    return precio > 0


def validar_unidades(unidades):
    return unidades >= 0


def agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex,
                   precio, unidades, d_prendas, d_bodega):
    if buscar_codigo(codigo, d_prendas):
        return False

    codigo = codigo.strip().upper()

    d_prendas[codigo] = [
        nombre.strip(),
        categoria.strip(),
        talla.strip(),
        color.strip(),
        material.strip(),
        es_unisex
    ]

    d_bodega[codigo] = [precio, unidades]

    return True


def eliminar_prenda(codigo, d_prendas, d_bodega):
    if buscar_codigo(codigo, d_prendas):
        codigo_real = obtener_codigo_real(codigo, d_prendas)
        del d_prendas[codigo_real]
        del d_bodega[codigo_real]
        return True

    return False


def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoria")
    print("2. Busqueda de prendas por rango de precio")
    print("3. Actualizar precio de prenda")
    print("4. Agregar prenda")
    print("5. Eliminar prenda")
    print("6. Salir")
    print("=====================================")


def programa_principal():
    prendas = {
        "S001": ["Polera Basica", "polera", "M", "negro", "algodon", True],
        "S002": ["Jeans Slim", "pantalon", "L", "azul", "denim", False],
        "S003": ["Chaqueta Urban", "chaqueta", "M", "gris", "poliester", True],
        "S004": ["Vestido Sol", "vestido", "S", "rojo", "lino", False],
        "S005": ["Poleron Cozy", "poleron", "XL", "verde", "algodon", True],
        "S006": ["Camisa Formal", "camisa", "M", "blanco", "algodon", False]
    }

    bodega = {
        "S001": [7990, 12],
        "S002": [19990, 0],
        "S003": [29990, 3],
        "S004": [24990, 6],
        "S005": [17990, 8],
        "S006": [14990, 2]
    }

    continuar = True

    while continuar:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            categoria = input("Ingrese categoria a consultar: ")

            if validar_categoria(categoria):
                unidades_categoria(categoria, prendas, bodega)
            else:
                print("La categoria no puede estar vacia")

        elif opcion == 2:
            datos_validos = False

            while not datos_validos:
                try:
                    precio_minimo = int(input("Ingrese precio minimo: "))
                    precio_maximo = int(input("Ingrese precio maximo: "))

                    if precio_minimo >= 0 and precio_maximo >= 0 and precio_minimo <= precio_maximo:
                        datos_validos = True
                    else:
                        print("El rango de precios no es valido")
                except ValueError:
                    print("Debe ingresar valores enteros")

            busqueda_precio(precio_minimo, precio_maximo, prendas, bodega)

        elif opcion == 3:
            actualizar_otro = "s"

            while actualizar_otro == "s":
                codigo_prenda = input("Ingrese código de la prenda: ")

                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))

                    if validar_precio(nuevo_precio):
                        resultado = actualizar_precio(
                            codigo_prenda,
                            nuevo_precio,
                            prendas,
                            bodega
                        )

                        if resultado:
                            print("Precio actualizado")
                        else:
                            print("El codigo no existe")
                    else:
                        print("El precio debe ser un numero entero mayor que cero")

                except ValueError:
                    print("El precio debe ser un numero entero mayor que cero")

                actualizar_otro = input(
                    "¿Desea actualizar otro precio (s/n)?: "
                ).strip().lower()

                while actualizar_otro != "s" and actualizar_otro != "n":
                    actualizar_otro = input(
                        "Debe ingresar s o n: "
                    ).strip().lower()

        elif opcion == 4:
            codigo_prenda = input("Ingrese codigo de la prenda: ")
            nombre = input("Ingrese nombre: ")
            categoria = input("Ingrese categoria: ")
            talla = input("Ingrese talla: ")
            color = input("Ingrese color: ")
            material = input("Ingrese material: ")
            respuesta_unisex = input("¿Es unisex? (s/n): ")

            try:
                precio = int(input("Ingrese precio: "))
                unidades = int(input("Ingrese unidades: "))

                if not validar_codigo(codigo_prenda):
                    print("El codigo no puede estar vacio")
                elif buscar_codigo(codigo_prenda, prendas):
                    print("El código ya existe")
                elif not validar_nombre(nombre):
                    print("El nombre no puede estar vacio")
                elif not validar_categoria(categoria):
                    print("La categoria no puede estar vacia")
                elif not validar_talla(talla):
                    print("La talla no puede estar vacia")
                elif not validar_color(color):
                    print("El color no puede estar vacio")
                elif not validar_material(material):
                    print("El material no puede estar vacio")
                elif not validar_es_unisex(respuesta_unisex):
                    print("Debe ingresar s o n en la opcion unisex")
                elif not validar_precio(precio):
                    print("El precio debe ser un numero entero mayor que cero")
                elif not validar_unidades(unidades):
                    print("Las unidades deben ser un numero entero mayor o igual a cero")
                else:
                    es_unisex = respuesta_unisex.strip().lower() == "s"

                    resultado = agregar_prenda(
                        codigo_prenda,
                        nombre,
                        categoria,
                        talla,
                        color,
                        material,
                        es_unisex,
                        precio,
                        unidades,
                        prendas,
                        bodega
                    )

                    if resultado:
                        print("Prenda agregada")
                    else:
                        print("El codigo ya existe")

            except ValueError:
                print("El precio y las unidades deben ser valores enteros")

        elif opcion == 5:
            codigo_prenda = input("Ingrese codigo de la prenda que desea eliminar: ")
            resultado = eliminar_prenda(codigo_prenda, prendas, bodega)

            if resultado:
                print("Prenda eliminada")
            else:
                print("El codigo no existe")

        elif opcion == 6:
            continuar = False
            print("Programa finalizado.")


programa_principal()