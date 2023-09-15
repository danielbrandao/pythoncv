# Importação das bibliotecas
import cv2
# Leitura da imagem com a função imread()
imagem = cv2.imread('placa-carro.jpg')
if imagem is None:
    print("Erro ao carregar imagem!")
    exit()
print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem

# Mostra a imagem com a função imshow
cv2.imshow("Nome da janela", imagem)
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida.jpg", imagem)
