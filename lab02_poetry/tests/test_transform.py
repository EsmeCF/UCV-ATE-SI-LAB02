import numpy as np
from image_processing.transform import convertir_grises, ajustar_brillo

def test_convertir_grises():
    imagen = np.zeros((10,10,3), dtype=np.uint8)
    resultado = convertir_grises(imagen)
    assert resultado.shape == (10,10)

def test_ajustar_brillo():
    imagen = np.zeros((10,10), dtype=np.uint8)
    resultado = ajustar_brillo(imagen, alpha=1.2, beta=30)
    assert resultado.shape == (10,10)