import cv2

def cargar_imagen(ruta: str):
    """Carga una imagen desde disco"""
    return cv2.imread(ruta)