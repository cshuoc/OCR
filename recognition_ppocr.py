from paddleocr import PaddleOCR,draw_ocr
from googletrans import Translator
from matplotlib import pyplot as plt
from PIL import Image 
import cv2 
import os 

def pic_to_txt(img_path : str,  pic_lang : str, target_lang : str):
    ppocr = PaddleOCR(lang= pic_lang ,use_gpu=False, use_angle_cls = True)
    image = cv2.imread(img_path)
    image = cv2.resize(image, (image.shape[0]*2, image.shape[1]*2), interpolation=cv2.INTER_AREA)
    result = ppocr.ocr(image)
    print(result)
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='C:/Users/user/Desktop/shuo/id_card/TaipeiSansTCBeta-Regular.ttf')
    im_show = Image.fromarray(im_show)
    plt.imshow(im_show)                   
    plt.show()
    print(result)
    for res in result:
        print(res[1][0])
    for res in result:
        text=res[1][0]
        translator = Translator()
        result = translator.translate(text, dest=target_lang, src = pic_lang)
        print(result.text)

if __name__ == "__main__":
    img_path = 'C:/Users/user/Desktop/shuo/OCR/ind_0.jpg'
    pic_lang = 'id'
    target_lang = 'zh-tw'
    pic_to_txt(img_path, pic_lang, target_lang)