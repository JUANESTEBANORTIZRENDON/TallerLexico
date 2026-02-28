# 01_COMO_PROBAR

## Requisitos
- Tener Python 3 instalado.

## Como ejecutar
1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta:

```bash
python main.py
```

## Datos de prueba automaticos
Al entrar en cada menu de estructura, se cargan automaticamente 10 numeros enteros aleatorios.
Esto permite probar operaciones sin tener que insertar todo a mano.

## Menu principal
Al iniciar, veras:
- `1` Probar Listas
- `2` Probar Pila
- `3` Probar Cola
- `4` Probar Arbol Binario
- `0` Salir

En cada opcion, hay un mini-menu para usar los metodos basicos.

## Ejemplos rapidos

### Listas
Al entrar en `1. Probar Listas`, veras un sub-menu:
- `1` Lista Ordenada (ascendente)
- `2` Lista Enlazada (simple)
- `3` Lista Doble Enlazada

Nota: los 10 datos aleatorios cambian en cada ejecucion, asi que tus numeros seran distintos.

#### Lista Ordenada
Ejemplo 1 (mostrar lista inicial ya ordenada):
```
Opcion: 1
Opcion: 5
Lista: [3, 7, 12, 18, 22, 37, 45, 61, 90, 95]
```
Ejemplo 2 (insertar y ver que se mantiene ordenada):
```
Opcion: 1
Valor: 15
Estado actual: [3, 7, 12, 15, 18, 22, 37, 45, 61, 90, 95]
```
Ejemplo 3 (buscar un valor):
```
Opcion: 3
Valor: 37
Indice: 6
```

#### Lista Enlazada (simple)
Ejemplo (mostrar lista; se ve con flechas):
```
Opcion: 2
Opcion: 6
Lista: [12 -> 7 -> 45 -> 3 -> 90 -> 18 -> 22 -> 61 -> 5 -> 37]
```

#### Lista Doble Enlazada
Ejemplo (mostrar y luego mostrar reversa):
```
Opcion: 3
Opcion: 6
Lista: [12 <-> 7 <-> 45 <-> 3 <-> 90 <-> 18 <-> 22 <-> 61 <-> 5 <-> 37]
Opcion: 7
Reversa: [37 <-> 5 <-> 61 <-> 22 <-> 18 <-> 90 <-> 3 <-> 45 <-> 7 <-> 12]
```

### Pila
Ejemplo 1:
```
Opcion: 1
Valor: 7
Estado actual: Pila: [7]
```
Ejemplo 2 (pila inicial con datos de prueba):
```
Opcion: 4
Pila: [12, 7, 45, 3, 90, 18, 22, 61, 5, 37]
```
Ejemplo 2:
```
Opcion: 2
Pop: 7
Estado actual: Pila: []
```

### Cola
Ejemplo 1:
```
Opcion: 1
Valor: 3
Estado actual: Cola: [3]
```
Ejemplo 2 (cola inicial con datos de prueba):
```
Opcion: 4
Cola: [12, 7, 45, 3, 90, 18, 22, 61, 5, 37]
```
Ejemplo 2:
```
Opcion: 2
Dequeue: 3
Estado actual: Cola: []
```

### Arbol Binario
Ejemplo 1:
```
Opcion: 1
Valor: 8
Opcion: 1
Valor: 3
Opcion: 1
Valor: 10
```
Ejemplo 2 (arbol inicial con datos de prueba):
```
Opcion: 3
Preorden : [12, 7, 3, 5, 45, 22, 18, 37, 90, 61]
Inorden  : [3, 5, 7, 12, 18, 22, 37, 45, 61, 90]
Postorden: [5, 3, 7, 18, 37, 22, 61, 90, 45, 12]
```
Ejemplo 2:
```
Opcion: 3
Preorden : [8, 3, 10]
Inorden  : [3, 8, 10]
Postorden: [3, 10, 8]
```
