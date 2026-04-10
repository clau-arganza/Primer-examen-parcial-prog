import threading
import queue
import time
import random


# Cola compartida para almacenar temporalmente las imágenes
cola_imagenes = queue.Queue()

# Número total de imágenes que vamos a simular
TOTAL_IMAGENES = 15       #esto me lo puse para que no se haga tan largo el proceso, pero se puede aumentar para ver más claramente la diferencia entre la llegada y el procesamiento de las imágenes

# Señal para indicar al consumidor que ya no llegarán más imágenes
FIN = object() 


def recibir_imagenes():
    """
    Función productora.
    Simula la llegada constante e impredecible de imágenes satelitales.
    """
    for i in range(1, TOTAL_IMAGENES + 1):
        # Simula que las imágenes llegan a intervalos impredecibles
        tiempo_llegada = random.uniform(0.2, 1.0)
        time.sleep(tiempo_llegada)

        imagen = f"imagen_{i}"
        cola_imagenes.put(imagen)

        print(f"[RECEPCIÓN] Ha llegado {imagen}. "
              f"Imágenes en cola: {cola_imagenes.qsize()}")

    # Avisamos de que ya no llegarán más imágenes
    cola_imagenes.put(FIN)
    print("[RECEPCIÓN] No llegarán más imágenes.")


def procesar_imagenes():
    """
    Función consumidora.
    Extrae imágenes de la cola y las procesa una a una.
    """
    while True:
        imagen = cola_imagenes.get()

        # Si recibimos la señal de fin, terminamos
        if imagen is FIN:
            cola_imagenes.task_done()
            print("[PROCESAMIENTO] No quedan más imágenes por procesar.")
            break

        print(f"[PROCESAMIENTO] Comenzando análisis de {imagen}...")

        # Simula que el procesamiento tarda bastante
        tiempo_procesamiento = random.uniform(1.5, 3.0)
        time.sleep(tiempo_procesamiento)

        print(f"[PROCESAMIENTO] {imagen} procesada correctamente.")

        cola_imagenes.task_done()


def main():
    # Creamos los hilos
    hilo_recepcion = threading.Thread(target=recibir_imagenes)
    hilo_procesamiento = threading.Thread(target=procesar_imagenes)

    # Iniciamos los hilos
    hilo_recepcion.start()
    hilo_procesamiento.start()

    # Esperamos a que termine la recepción
    hilo_recepcion.join()

    # Esperamos a que se vacíe la cola completamente
    cola_imagenes.join()

    # Esperamos a que termine el procesamiento
    hilo_procesamiento.join()

    print("\n[SISTEMA] Todas las imágenes han sido recibidas y procesadas.")


if __name__ == "__main__":
    main()