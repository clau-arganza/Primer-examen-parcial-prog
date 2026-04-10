Sistema de procesamiento de imágenes satelitales
Descripción:
Este programa simula un sistema concurrente de recepción y procesamiento de imágenes satelitales en Python.
El sistema está dividido en dos partes:
- Recepción de imágenes: las imágenes llegan de forma continua e impredecible.
- Procesamiento de imágenes: las imágenes almacenadas se procesan una a una.
- 
Para resolver el problema se ha utilizado el patrón producer-consumer:

- Productor: la parte del programa que recibe imágenes.
- Consumidor: la parte del programa que procesa imágenes.

Entre ambas partes se utiliza una cola FIFO (`queue.Queue()`), que actúa como almacenamiento temporal.

Se utilizan hilos (`threading`) porque el objetivo es que la recepción y el procesamiento funcionen de forma concurrente dentro del mismo programa.

De esta forma:
- un hilo puede seguir recibiendo imágenes
- mientras otro hilo procesa las que ya han llegado

Además, como ambos comparten la misma cola en memoria, el uso de hilos resulta adecuado y sencillo para este ejercicio.

Se utiliza una cola FIFO porque:
- evita la pérdida de imágenes cuando llegan más rápido de lo que se procesan
- mantiene el orden de llegada

Así, si en un momento entran muchas imágenes, quedan almacenadas en espera hasta que el consumidor pueda procesarlas.

No es necesario instalar librerías externas, ya que solo se usan módulos estándar de Python:
- `threading`
- `queue`
- `time`
- `random`

Archivos
- `codigo.py` → programa principal
