# 02_EXPLICACION_ESTRUCTURAS

## Listas (3 variantes)
En este mini-proyecto se muestran 3 formas comunes de representar una "lista":

### 1) Lista Ordenada (arreglo / lista de Python por dentro)
Es una lista lineal que SIEMPRE se mantiene ordenada (ascendente).

Idea clave:
- La insercion se hace "por valor" para no romper el orden.
- Como esta ordenada, buscar puede hacerse con busqueda binaria.

Operaciones tipicas:
- insertar(valor) manteniendo el orden
- eliminar_en(indice)
- buscar(valor) (binaria)
- obtener(indice)

Uso (pseudocodigo):
```
lista.insertar(10)
lista.insertar(5)       # queda [5, 10]
pos = lista.buscar(10)
```

### 2) Lista Enlazada Simple
Cada nodo guarda un valor y un enlace al siguiente nodo.

Diferencias principales vs arreglo:
- No hay acceso directo por indice: obtener(i) recorre desde el inicio (O(n)).
- Insertar/eliminar al inicio es muy barato (O(1)), pero en medio requiere recorrer.

Uso (pseudocodigo):
```
lista.agregar_al_final(10)
lista.insertar_en(0, 5)
valor = lista.obtener(1)   # 10
```

### 3) Lista Doble Enlazada
Cada nodo tiene dos enlaces: anterior y siguiente.

Diferencias principales vs enlazada simple:
- Puedes recorrer hacia adelante y hacia atras.
- Eliminar/insertar alrededor de un nodo es mas comodo porque hay enlace al anterior.
- Usa un poco mas de memoria (dos enlaces por nodo).

Uso (pseudocodigo):
```
lista.agregar_al_final(1)
lista.agregar_al_final(2)
print(lista.mostrar_reversa())  # [2 <-> 1]
```

## Pila (Stack)
Una pila sigue el principio LIFO (Last In, First Out).
Se usa en parsing de expresiones, verificacion de parentesis y evaluacion.

Operaciones basicas:
- push (insertar en la cima)
- pop (sacar de la cima)
- peek (ver la cima)

Ejemplo:
```
pila.push(4)
pila.push(9)
tope = pila.pop()   # 9
```

## Cola (Queue)
Una cola sigue el principio FIFO (First In, First Out).
Se usa en planificacion de procesos y manejo de tareas en espera.

Operaciones basicas:
- enqueue (insertar al final)
- dequeue (sacar del frente)
- front (ver el frente)

Ejemplo:
```
cola.enqueue(1)
cola.enqueue(2)
primero = cola.dequeue()  # 1
```

## Arbol Binario
Un arbol binario tiene nodos con hasta dos hijos: izquierdo y derecho.
En un BST, los menores van a la izquierda y los mayores a la derecha.
Se usa para representar expresiones (AST) y busquedas eficientes.

Operaciones basicas:
- insertar
- buscar
- recorrer

Recorridos:
- Preorden: raiz, izquierdo, derecho
- Inorden: izquierdo, raiz, derecho
- Postorden: izquierdo, derecho, raiz

Ejemplo:
```
arbol.insertar(8)
arbol.insertar(3)
arbol.insertar(10)
print(arbol.inorden())  # [3, 8, 10]
```
