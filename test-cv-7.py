from PIL import Image
import pyocr
import pyocr.builders

# Inicializar o OCR com Tesseract
tools = pyocr.get_available_tools()
if len(tools) == 0:
    raise Exception("Nenhum mecanismo OCR disponível")
tool = tools[0]

# Carregar a imagem a ser reconhecida
image = Image.open("placa-carro.jpg")

# Realizar o reconhecimento de texto
text = tool.image_to_string(
    image,
    lang='por',  # Idioma (ajuste conforme necessário)
    builder=pyocr.builders.TextBuilder()
)

print(text)
