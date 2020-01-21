import cv2
import pytesseract 

img = cv2.imread('./numperPlate/numperc.png', cv2.IMREAD_GRAYSCALE)
print(img.shape)

getNumber = pytesseract.image_to_data(img, lang='eng',  config='--oem 3')
print(getNumber)

cv2.imshow('windoneam', img)
cv2.waitKey(0)
cv2.destroyAllWindows()












# sudo apt-get install tesseract-ocr

