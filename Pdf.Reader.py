import pytesseract
import cv2

imagem = cv2.imread('C:\Pedro\sigmativa\convertToPDF\env\Teste1')

caminho = r"C:\Program Files\Tesseract-OCR"

pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
text = pytesseract.image_to_string(imagem)

print(text)
