import cv2
import numpy as np

# Carrega a imagem
image = cv2.imread("placa-carro.jpg")

# Verifica se a imagem foi carregada corretamente
if image is None:
    raise ValueError("Imagem não encontrada")

# Converte a imagem para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplica um filtro Gaussiano para suavizar a imagem
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Aplica um threshold para binarizar a imagem
thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)[1]

# Identifica os contornos da imagem
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Encontra o contorno do texto
largest_contour = max(contours, key=cv2.contourArea)

# Extrai os pontos do contorno
x, y, w, h = cv2.boundingRect(largest_contour)

# Converte o contorno para um array numpy
text_box = thresh[y:y + h, x:x + w]

# Aplica um filtro de contraste à imagem
contrast_image = cv2.addWeighted(text_box, 2, text_box, 0, 0)

# Converte os elementos do array numpy para strings
text_box = np.char.decode(contrast_image)

# Remove os espaços em branco do array numpy
text = "".join(text_box.flatten())

# Imprime o texto reconhecido
print(text)
