from paddleocr import PaddleOCR, draw_ocr
from googletrans import Translator
from matplotlib import pyplot as plt
from PIL import Image 
import cv2 
import os 
import numpy as np

def pic_to_txt(img_path : str,  pic_lang : str, rec_lng : str, target_lang : str):
    ppocr = PaddleOCR(lang = pic_lang, use_angle_cls=True,  structure_version='PP-OCRv3', cls_model_dir = 'ch_ppocr_mobile_v2.0_cls')
    image = cv2.imread(img_path)
     # 將圖片轉換為灰度圖像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # # 二值化處理
    # _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # 顯示處理後的圖像
    cv2.imshow('Preprocessed Image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    result = ppocr.ocr(gray)
    print(result)
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='C:/Users/user/Desktop/shuo/OCR/ppocr/TaipeiSansTCBeta-Regular.ttf')
    im_show = Image.fromarray(im_show)
    plt.imshow(im_show)                   
    plt.show()
    # print(result)
    merge_result = []
    for res in result:
        # print(res[1][0])
        merge_result.append(res[1][0])
    # 將列表中的所有字符串合併成一個字串
    merge_result = ' '.join(merge_result)
    print(merge_result)

    translator = Translator()
    result = translator.translate(merge_result, dest=target_lang, src = rec_lng)
    print(result.text)
    

if __name__ == "__main__":
    img_path = 'C:/Users/user/Desktop/shuo/OCR/english_1.jpg'
    pic_lang = 'en'
    rec_lng = 'en'
    target_lang = 'zh-TW'
    pic_to_txt(img_path, pic_lang, rec_lng, target_lang)
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='文字識別及翻譯')
    parser.add_argument('--image_path', type=str, default="/your/path/pic", help='欲辨識圖像路徑')
    parser.add_argument('--result_text_path', type=str, default='/your/path/text.txt', help='辨識結果儲存路徑')
    parser.add_argument('--pic_lang', type=str, default='en', help='欲辨識圖像文字類型')
    parser.add_argument('--rec_lng', type=str, default='en', help='欲辨識圖像結果的文字類型')
    parser.add_argument('--target_lang', type=str, default='chinese_cht', help='欲翻譯文字類型')
    parser.add_argument('--gpu', type=bool, default=False, help='是否使用gpu')
    
    args = parser.parse_args()    
    
    pic_to_txt(args.img_path, args.result_text_path, args.pic_lang, args.rec_lng, args.target_lang, args.gpu)
