import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread('imagen_prueba.jpg')

imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

plt.imshow(imagen_rgb)
plt.title("Imagen Original")
plt.axis("off")
plt.show()

gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

plt.imshow(gris, cmap='gray')
plt.title("Escala de Grises")
plt.axis("off")
plt.show()

brillo = cv2.convertScaleAbs(gris, alpha=1.5, beta=50)

plt.imshow(brillo, cmap='gray')
plt.title("Brillo Ajustado")
plt.axis("off")
plt.show()