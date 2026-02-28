"""
Programa principal para probar estructuras de datos desde consola.
"""

import random

from estructuras.lista import Lista
from estructuras.lista_enlazada import ListaEnlazada
from estructuras.lista_doble_enlazada import ListaDobleEnlazada
from estructuras.pila import Pila
from estructuras.cola import Cola
from estructuras.arbol_binario import ArbolBinario


def leer_entero(mensaje):
    """Lee un entero desde consola con validacion simple."""
    try:
        return int(input(mensaje))
    except ValueError:
        print("Entrada invalida. Debe ser un numero entero.")
        return None


def menu_lista_ordenada():
    lista = Lista()
    for valor in generar_datos_prueba():
        lista.insertar(valor)
    while True:
        print("\n--- MENU LISTA ORDENADA ---")
        print("1. Insertar (mantiene orden)")
        print("2. Eliminar en indice")
        print("3. Buscar valor")
        print("4. Obtener en indice")
        print("5. Mostrar lista")
        print("6. Tamano")
        print("0. Volver")
        opcion = input("Opcion: ")

        if opcion == "1":
            valor = leer_entero("Valor: ")
            if valor is not None:
                lista.insertar(valor)
        elif opcion == "2":
            indice = leer_entero("Indice: ")
            if indice is not None:
                eliminado = lista.eliminar_en(indice)
                print("Eliminado:", eliminado)
        elif opcion == "3":
            valor = leer_entero("Valor: ")
            if valor is not None:
                indice = lista.buscar(valor)
                print("Indice:", indice)
        elif opcion == "4":
            indice = leer_entero("Indice: ")
            if indice is not None:
                valor = lista.obtener(indice)
                print("Valor:", valor)
        elif opcion == "5":
            print("Lista:", lista.mostrar())
        elif opcion == "6":
            print("Tamano:", lista.tamano())
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")

        print("Estado actual:", lista.mostrar())


def menu_lista_enlazada():
    lista = ListaEnlazada()
    for valor in generar_datos_prueba():
        lista.agregar_al_final(valor)
    while True:
        print("\n--- MENU LISTA ENLAZADA (SIMPLE) ---")
        print("1. Agregar al final")
        print("2. Insertar en indice")
        print("3. Eliminar en indice")
        print("4. Buscar valor")
        print("5. Obtener en indice")
        print("6. Mostrar lista")
        print("7. Tamano")
        print("0. Volver")
        opcion = input("Opcion: ")

        if opcion == "1":
            valor = leer_entero("Valor: ")
            if valor is not None:
                lista.agregar_al_final(valor)
        elif opcion == "2":
            indice = leer_entero("Indice: ")
            valor = leer_entero("Valor: ")
            if indice is not None and valor is not None:
                lista.insertar_en(indice, valor)
        elif opcion == "3":
            indice = leer_entero("Indice: ")
            if indice is not None:
                eliminado = lista.eliminar_en(indice)
                print("Eliminado:", eliminado)
        elif opcion == "4":
            valor = leer_entero("Valor: ")
            if valor is not None:
                indice = lista.buscar(valor)
                print("Indice:", indice)
        elif opcion == "5":
            indice = leer_entero("Indice: ")
            if indice is not None:
                valor = lista.obtener(indice)
                print("Valor:", valor)
        elif opcion == "6":
            print("Lista:", lista.mostrar())
        elif opcion == "7":
            print("Tamano:", lista.tamano())
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")

        print("Estado actual:", lista.mostrar())


def menu_lista_doble_enlazada():
    lista = ListaDobleEnlazada()
    for valor in generar_datos_prueba():
        lista.agregar_al_final(valor)
    while True:
        print("\n--- MENU LISTA DOBLE ENLAZADA ---")
        print("1. Agregar al final")
        print("2. Insertar en indice")
        print("3. Eliminar en indice")
        print("4. Buscar valor")
        print("5. Obtener en indice")
        print("6. Mostrar (cabeza a cola)")
        print("7. Mostrar reversa (cola a cabeza)")
        print("8. Tamano")
        print("0. Volver")
        opcion = input("Opcion: ")

        if opcion == "1":
            valor = leer_entero("Valor: ")
            if valor is not None:
                lista.agregar_al_final(valor)
        elif opcion == "2":
            indice = leer_entero("Indice: ")
            valor = leer_entero("Valor: ")
            if indice is not None and valor is not None:
                lista.insertar_en(indice, valor)
        elif opcion == "3":
            indice = leer_entero("Indice: ")
            if indice is not None:
                eliminado = lista.eliminar_en(indice)
                print("Eliminado:", eliminado)
        elif opcion == "4":
            valor = leer_entero("Valor: ")
            if valor is not None:
                indice = lista.buscar(valor)
                print("Indice:", indice)
        elif opcion == "5":
            indice = leer_entero("Indice: ")
            if indice is not None:
                valor = lista.obtener(indice)
                print("Valor:", valor)
        elif opcion == "6":
            print("Lista:", lista.mostrar())
        elif opcion == "7":
            print("Reversa:", lista.mostrar_reversa())
        elif opcion == "8":
            print("Tamano:", lista.tamano())
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")

        print("Estado actual:", lista.mostrar())


def menu_listas():
    while True:
        print("\n--- MENU LISTAS ---")
        print("1. Lista Ordenada (ascendente)")
        print("2. Lista Enlazada (simple)")
        print("3. Lista Doble Enlazada")
        print("0. Volver")
        opcion = input("Opcion: ")

        if opcion == "1":
            menu_lista_ordenada()
        elif opcion == "2":
            menu_lista_enlazada()
        elif opcion == "3":
            menu_lista_doble_enlazada()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")


def menu_pila():
    pila = Pila()
    for valor in generar_datos_prueba():
        pila.push(valor)
    while True:
        print("\n--- MENU PILA ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Mostrar pila")
        print("0. Volver")
        opcion = input("Opcion: ")

        if opcion == "1":
            valor = leer_entero("Valor: ")
            if valor is not None:
                pila.push(valor)
        elif opcion == "2":
            valor = pila.pop()
            print("Pop:", valor)
        elif opcion == "3":
            valor = pila.peek()
            print("Peek:", valor)
        elif opcion == "4":
            print(pila.mostrar())
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")

        print("Estado actual:", pila.mostrar())


def menu_cola():
    cola = Cola()
    for valor in generar_datos_prueba():
        cola.enqueue(valor)
    while True:
        print("\n--- MENU COLA ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Mostrar cola")
        print("0. Volver")
        opcion = input("Opcion: ")

        if opcion == "1":
            valor = leer_entero("Valor: ")
            if valor is not None:
                cola.enqueue(valor)
        elif opcion == "2":
            valor = cola.dequeue()
            print("Dequeue:", valor)
        elif opcion == "3":
            valor = cola.front()
            print("Front:", valor)
        elif opcion == "4":
            print(cola.mostrar())
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")

        print("Estado actual:", cola.mostrar())


def menu_arbol():
    arbol = ArbolBinario()
    for valor in generar_datos_prueba():
        arbol.insertar(valor)
    while True:
        print("\n--- MENU ARBOL BINARIO ---")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Mostrar recorridos")
        print("0. Volver")
        opcion = input("Opcion: ")

        if opcion == "1":
            valor = leer_entero("Valor: ")
            if valor is not None:
                arbol.insertar(valor)
        elif opcion == "2":
            valor = leer_entero("Valor: ")
            if valor is not None:
                encontrado = arbol.buscar(valor)
                print("Encontrado:", encontrado)
        elif opcion == "3":
            arbol.mostrar_recorridos()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")


def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Probar Listas")
        print("2. Probar Pila")
        print("3. Probar Cola")
        print("4. Probar Arbol Binario")
        print("0. Salir")
        opcion = input("Opcion: ")

        if opcion == "1":
            menu_listas()
        elif opcion == "2":
            menu_pila()
        elif opcion == "3":
            menu_cola()
        elif opcion == "4":
            menu_arbol()
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opcion invalida.")


def generar_datos_prueba():
    """Genera 10 numeros enteros aleatorios simples para pruebas."""
    return [random.randint(1, 99) for _ in range(10)]


if __name__ == "__main__":
    main()
