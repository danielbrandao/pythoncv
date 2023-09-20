import cv2
import pytesseract
from PIL import Image
import string
import re

# Carrega a imagem da placa de carro
img2 = cv2.imread("placa-carro.jpg")

# Converte a imagem para preto e branco
img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Aplicar um algoritmo de thresholding para separar a placa de carro do fundo
thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Extrai o texto da placa de carro usando o OCR
texto_placa = pytesseract.image_to_string(thresh, lang="pt")

# Imprime o texto da placa de carro na tela
print(texto_placa)
