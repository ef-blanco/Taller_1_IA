import pickle
import os
import glob

# Importante: Importar las clases para que Python entienda qué está cargando
from world.rescue_layout import RescueLayout
from world.game import Grid


def leer_ultima_grabacion():
    # Buscar cualquier archivo que empiece por recorded-episode
    archivos = glob.glob("recorded-episode*")
    
    if not archivos:
        print("No se encontraron archivos de grabación.")
        return
    
    # Elegir el archivo más recientemente modificado
    ultimo_archivo = max(archivos, key=os.path.getmtime)
    
    print(f"\nAbriendo el archivo más reciente encontrado: {ultimo_archivo}")
    
    try:
        with open(ultimo_archivo, 'rb') as f:
            datos = pickle.load(f)
            
            layout = datos['layout']
            acciones = datos['actions']
            
            print("\n--- RESUMEN DE LA MISIÓN ---")
            print(f"Mapa cargado: {layout.width}x{layout.height}")
            print(f"Sobrevivientes rescatados: {len(layout.survivors.asList())}")
            print(f"Número total de movimientos: {len(acciones)}")
            
            print("\n--- LISTA DE ACCIONES ---")
            print(acciones)
            
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")


if __name__ == "__main__":
    leer_ultima_grabacion()