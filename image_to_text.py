import numpy as np
from pytesseract import Output
import pytesseract
import cv2
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'D:\\ProgramFile\\Tesseract\\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "D:\\ProgramFile\\Tesseract\\tessdata"'

if __name__ == '__main__':

    # Read the image
    filename = 'screenshot.png'
    img = np.array(Image.open(filename))
    
    
    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)

    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
    img = cv2.GaussianBlur(img, (1, 1), 0)
    
    text = pytesseract.image_to_string(grayImage,lang='eng')

    print(text)


def image_to_text(image_path,language='eng'):
    img = np.array(Image.open(image_path))
    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)

    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    text = pytesseract.image_to_string(grayImage,lang='eng',config=tessdata_dir_config)

    return text