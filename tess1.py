import cv2
import pytesseract
#giving tesseract-ocr install(.exe) file path 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
config=('-l eng --oem 1 --psm 3')

img=cv2.imread('C:\\Users\ABHILASH\Pictures\id.jpg')
text=pytesseract.image_to_string(img,config=config)

print(text)
