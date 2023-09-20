import cv2
import pytesseract

def extrair_texto_placa(imagem):
    # Converte a imagem para preto e branco
    imagem_preto_e_branco = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Encontrar a região da placa de carro na imagem
    placa = cv2.findContours(imagem_preto_e_branco, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    placa = placa[0]

    # Aplicar um algoritmo de segmentação para separar a placa de carro da imagem
    placa = cv2.threshold(imagem, 200, 255, cv2.THRESH_BINARY)[1]

    # Aplicar o OCR na região da placa de carro
    texto_placa = pytesseract.image_to_string(placa, lang="pt")

    return texto_placa


if __name__ == "__main__":
    # Carrega a imagem da placa de carro
    imagem = cv2.imread("placa-carro.jpg")

    # Extrai o texto da placa de carro
    texto_placa = extrair_texto_placa(imagem)

    # Imprime o texto da placa de carro
    print(texto_placa)